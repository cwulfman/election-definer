from pathlib import Path

import pytest


# --- Paths

# Hardcoded. Better to use an environment variable, or get it from version control.
_HERE = Path(__file__)
# Assumes we are in 'test/py/tests'
_ROOT_PATH = (_HERE.parent / Path("../../..")).resolve()


class Paths:

    ROOT = _ROOT_PATH
    SOURCES = ROOT
    DATA = ROOT / "test" / "data"
    INPUTS = DATA
    OUTPUTS = DATA
