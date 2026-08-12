"""Standalone command-line interface for inep-fetcher."""

import sys

from .plugin import app


def main(argv: list[str] | None = None) -> None:
    """Run the standalone command-line interface.

    Args:
        argv: Optional list of command-line arguments to use instead of sys.argv.
    """
    if argv is not None:
        sys.argv = [sys.argv[0]] + argv
    try:
        app()
    except KeyboardInterrupt:
        sys.exit(130)
