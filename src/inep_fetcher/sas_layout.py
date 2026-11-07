"""Leitor do layout de largura fixa dos scripts SAS dos microdados antigos do INEP.

Os microdados do SAEB de 1995 a 2005 vêm em TXT de largura fixa, acompanhados
de um script SAS (``INPUT_SAS_*.sas``; em 2005, ``IMPUT_SAS_*.sas``) que diz
onde cada campo começa e termina:

    INFILE 'D:\\DADOS\\ALUNOS\\MATEMATICA_04SERIE.TXT' LRECL=327 MISSOVER;
    INPUT
    @1   MASCARA  8.     /*Número de acesso*/
    @9   PESO     12.5   /*Peso*/
    @21  UF       $Char2.;

Este módulo lê só a estrutura (``INFILE``, ``LRECL`` e o bloco ``INPUT``);
não interpreta o resto da linguagem SAS. Só biblioteca padrão.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field, replace

# Comentários /* ... */ viram marcadores antes de procurar INFILE/INPUT, para
# que um ";" ou a palavra INPUT dentro de um rótulo não confunda a leitura,
# mas o texto do rótulo ainda possa ser recuperado.
_COMMENT = re.compile(r"/\*(.*?)\*/", re.DOTALL)
_MARK = re.compile(r"\x00(\d+)\x00")
_INFILE = re.compile(r"\bINFILE\b\s*(?:(['\"])(?P<path>.*?)\1|(?P<bare>[^\s;]+))", re.I)
_LRECL = re.compile(r"\bLRECL\s*=\s*(\d+)", re.I)
_INPUT = re.compile(r"\bINPUT\b", re.I)
_AT = re.compile(r"@")
_FIELD = re.compile(
    r"@\s*(?P<start>\d+)\s+(?P<name>[A-Za-z_]\w*)\s+"
    r"(?P<char>\$)?\s*(?P<prefix>[A-Za-z]*?)(?P<width>\d+)\.(?P<dec>\d*)"
    r"(?:\s*\x00(?P<label>\d+)\x00)?"
)


@dataclass(frozen=True)
class SasField:
    """Um campo do registro: posição 1-based, largura e tipo."""

    name: str
    start: int
    width: int
    numeric: bool
    decimals: int = 0
    label: str = ""

    @property
    def end(self) -> int:
        """Última posição (1-based, inclusiva) do campo."""
        return self.start + self.width - 1


@dataclass(frozen=True)
class LayoutFix:
    """Correção de um script SAS inconsistente com os próprios dados.

    Desloca ``delta`` colunas todos os campos a partir de ``from_field``. Só
    vale se os dados confirmarem: ``dotted`` são campos com ponto decimal em
    toda linha não vazia e ``ranges`` dá a faixa inteira de cada campo.
    """

    from_field: str
    delta: int
    dotted: tuple[str, ...] = ()
    ranges: dict[str, tuple[int, int]] = field(default_factory=dict)


# (ano, nome do INFILE em minúsculas) -> correção. O script do INEP do SAEB 1999
# (escolas) declara ESTRATO @23 com largura 9 e UPA @31: os campos se
# sobrepõem. Nos dados, o estrato ocupa 23-31 e a UPA e o resto vêm uma coluna
# adiante. Não vale para nenhum outro arquivo.
LAYOUT_FIXES: dict[tuple[int, str], LayoutFix] = {
    (1999, "escolas_99.txt"): LayoutFix(
        from_field="upa",
        delta=1,
        dotted=("peso_ec",),
        ranges={"dep_adm": (1, 4), "local": (1, 2)},
    ),
}


@dataclass(frozen=True)
class SasLayout:
    """Layout de um TXT: nome do arquivo no ``INFILE``, ``LRECL`` e campos."""

    infile: str
    lrecl: int
    fields: list[SasField] = field(default_factory=list)
    fix: LayoutFix | None = None


def infile_name(path: str) -> str:
    """Nome do arquivo de um caminho do Windows (ou Unix), em minúsculas."""
    return re.split(r"[\\/]", path.strip())[-1].lower()


def peek_infile(text: str) -> str | None:
    """Nome do arquivo do ``INFILE`` (em minúsculas), mesmo de script inválido."""
    match = _INFILE.search(_COMMENT.sub(" ", text))
    if not match:
        return None
    return infile_name(match["path"] if match["path"] is not None else match["bare"])


def parse_sas_input(text: str, fix: LayoutFix | None = None) -> SasLayout:
    """Lê o ``INFILE``/``LRECL`` e o bloco ``INPUT`` de um script SAS.

    Campo que começa no ``LRECL`` ou depois (fim do registro) é aceito: com
    ``MISSOVER`` o SAS o lê como ausente. ``fix`` aplica uma correção de
    ``LAYOUT_FIXES`` antes de validar.

    Raises:
        ValueError: script sem ``INFILE``, ``LRECL`` ou campos; informato não
            reconhecido; nome de campo repetido; campos que se sobrepõem ou
            passam do ``LRECL``.
    """
    labels: list[str] = []

    def _stash(match: re.Match[str]) -> str:
        labels.append(" ".join(match.group(1).split()))
        return f" \x00{len(labels) - 1}\x00 "

    body = _COMMENT.sub(_stash, text)

    infile = _INFILE.search(body)
    if not infile:
        raise ValueError("script SAS sem INFILE")
    lrecl = _LRECL.search(body)
    if not lrecl:
        raise ValueError("script SAS sem LRECL")
    lrecl_n = int(lrecl.group(1))

    start = _INPUT.search(body, infile.end())
    if not start:
        raise ValueError("script SAS sem bloco INPUT")
    end = body.find(";", start.end())
    block = body[start.end() : end if end != -1 else len(body)]

    fields: list[SasField] = []
    for m in _FIELD.finditer(block):
        prefix = m["prefix"].lower()
        numeric = not m["char"] and prefix in {"", "best", "comma", "f"}
        if not m["char"] and not numeric:
            raise ValueError(f"informato não suportado no campo {m['name']}")
        label = labels[int(m["label"])] if m["label"] else ""
        fields.append(
            SasField(
                name=m["name"].lower(),
                start=int(m["start"]),
                width=int(m["width"]),
                numeric=numeric,
                decimals=int(m["dec"] or 0) if numeric else 0,
                label=label,
            )
        )
    if not fields:
        raise ValueError("bloco INPUT sem campos")
    if len(_AT.findall(block)) != len(fields):
        raise ValueError("bloco INPUT com campo em formato não reconhecido")

    if fix is not None:
        if not any(f.name == fix.from_field for f in fields):
            raise ValueError(f"correção de layout: campo {fix.from_field} ausente")
        shifting = False
        shifted = []
        for f in sorted(fields, key=lambda f: f.start):
            shifting = shifting or f.name == fix.from_field
            shifted.append(replace(f, start=f.start + fix.delta) if shifting else f)
        fields = shifted

    names: set[str] = set()
    for f in fields:
        if f.width < 1 or f.start < 1:
            raise ValueError(f"campo {f.name}: posição ou largura inválida")
        if f.name in names:
            raise ValueError(f"campo repetido: {f.name}")
        names.add(f.name)
    ordered = sorted(fields, key=lambda f: f.start)
    for prev, cur in zip(ordered, ordered[1:], strict=False):
        if cur.start <= prev.end:
            raise ValueError(
                f"campos {prev.name} ({prev.start}-{prev.end}) e {cur.name} "
                f"({cur.start}-{cur.end}) se sobrepõem"
            )
    for f in ordered:
        if f.end > lrecl_n and f.start < lrecl_n:
            raise ValueError(
                f"campo {f.name} termina na posição {f.end}, além do LRECL {lrecl_n}"
            )
    path = infile["path"] if infile["path"] is not None else infile["bare"]
    return SasLayout(infile=infile_name(path), lrecl=lrecl_n, fields=ordered, fix=fix)
