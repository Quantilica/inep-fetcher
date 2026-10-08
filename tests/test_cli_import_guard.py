"""Tests for inep_fetcher.cli import guard (host absent)."""

import importlib
import sys
import types

import pytest

import inep_fetcher.cli as cli_module

_PLUGIN_KEY = "inep_fetcher.plugin"


@pytest.fixture
def plugin_bloqueado():
    """Simular host ausente (typer e quantilica.cli.sdk bloqueados) e recarregar cli.

    O plugin do inep importa o host via ``quantilica.cli.sdk`` (sem ``import
    typer`` direto); bloquear só ``typer`` não quebraria o reimport porque o
    SDK já está em ``sys.modules``. Restaura tudo ao final.
    """
    saved_host = {key: sys.modules.get(key) for key in ("typer", "quantilica.cli.sdk")}
    had_plugin = _PLUGIN_KEY in sys.modules
    saved_plugin = sys.modules.get(_PLUGIN_KEY)
    sys.modules["typer"] = None
    sys.modules["quantilica.cli.sdk"] = None
    sys.modules.pop(_PLUGIN_KEY, None)  # forcar reimport do plugin
    importlib.reload(cli_module)
    yield cli_module
    for key, saved in saved_host.items():
        if saved is None:
            sys.modules.pop(key, None)
        else:
            sys.modules[key] = saved
    if had_plugin:
        sys.modules[_PLUGIN_KEY] = saved_plugin
    else:
        sys.modules.pop(_PLUGIN_KEY, None)
    importlib.reload(cli_module)


def test_importar_cli_sem_host_nao_levanta_module_not_found(plugin_bloqueado):
    assert plugin_bloqueado.app is None
    assert plugin_bloqueado._PLUGIN_ERROR is not None


def test_main_sem_host_sai_com_codigo_1_e_mensagem(plugin_bloqueado, capsys):
    with pytest.raises(SystemExit) as excinfo:
        plugin_bloqueado.main(["sync"])
    assert excinfo.value.code == 1
    saida = capsys.readouterr().err
    assert "Erro: CLI requer 'typer' e 'rich' (via quantilica-cli)." in saida
    assert 'Instale via "quantilica install inep".' in saida
    assert "Detalhe:" in saida


def test_importerror_interno_do_plugin_propaga():
    """ImportError de modulo fora do host (bug interno) nao vira exit 1: propaga."""
    saved = sys.modules.get(_PLUGIN_KEY)
    stub = types.ModuleType(_PLUGIN_KEY)

    def __getattr__(name):
        raise ModuleNotFoundError("No module named 'outro_modulo'", name="outro_modulo")

    stub.__getattr__ = __getattr__
    sys.modules[_PLUGIN_KEY] = stub
    try:
        with pytest.raises(ModuleNotFoundError):
            importlib.reload(cli_module)
    finally:
        if saved is None:
            sys.modules.pop(_PLUGIN_KEY, None)
        else:
            sys.modules[_PLUGIN_KEY] = saved
        importlib.reload(cli_module)
