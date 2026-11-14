"""Gera um RAR5 mínimo (membros só armazenados) sem depender do utilitário ``rar``."""

from __future__ import annotations

import zlib

_SIGNATURE = b"Rar!\x1a\x07\x01\x00"


def _vint(value: int) -> bytes:
    out = bytearray()
    while True:
        low = value & 0x7F
        value >>= 7
        if value:
            out.append(low | 0x80)
        else:
            out.append(low)
            return bytes(out)


def _block(body: bytes) -> bytes:
    """CRC32 + tamanho do cabeçalho + cabeçalho (``body`` = do tipo em diante)."""
    size = _vint(len(body))
    crc = zlib.crc32(size + body) & 0xFFFFFFFF
    return crc.to_bytes(4, "little") + size + body


def build_rar5(members: dict[str, bytes]) -> bytes:
    """RAR5 com os ``members`` (caminho -> conteúdo) sem compressão."""
    out = bytearray(_SIGNATURE)
    out += _block(_vint(1) + _vint(0) + _vint(0))  # cabeçalho principal
    for name, data in members.items():
        raw = name.encode("utf-8")
        body = (
            _vint(2)  # tipo: arquivo
            + _vint(0x2)  # flags do bloco: área de dados
            + _vint(len(data))  # tamanho da área de dados
            + _vint(0x4)  # flags do arquivo: CRC32 presente
            + _vint(len(data))  # tamanho descompactado
            + _vint(0x20)  # atributos
            + (zlib.crc32(data) & 0xFFFFFFFF).to_bytes(4, "little")
            + _vint(0)  # método 0 (armazenado)
            + _vint(0)  # SO de origem (Windows)
            + _vint(len(raw))
            + raw
        )
        out += _block(body) + data
    out += _block(_vint(5) + _vint(0) + _vint(0))  # fim do arquivo
    return bytes(out)
