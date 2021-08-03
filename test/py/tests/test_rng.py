from pathlib import Path

import lxml.etree

import pytest


# This file
_HERE = Path(__file__)
# Assume we are in 'test/py/tests'
_ROOT_PATH = (_HERE.parent / Path("../../..")).resolve()
# Transforms and schemas
_SOURCE_PATH = _ROOT_PATH
# Test data
_DATA_PATH = _ROOT_PATH / "test" / "data"
# Test inputs
_INPUTS_PATH = _DATA_PATH
# Expected results
_EXPECTED_PATH = _DATA_PATH

_RNG_FILE = _DATA_PATH / "electiondefinition.rng"


def test_validate_election_definitions():
    """Test that simplified election definitions validate under the RNG schema."""
    rng_file = _RNG_FILE
    input_path = _INPUTS_PATH

    # Load schema
    with rng_file.open("rb") as file:
        text = file.read()
    xml = lxml.etree.XML(text)
    rng = lxml.etree.RelaxNG(xml)

    # Load sources
    xml_files = sorted(input_path.glob("*.in.xml"))
    for xml_file in xml_files:
        with xml_file.open("rb") as file:
            text = file.read()
        input_ = lxml.etree.XML(text)
        assert rng.validate(input_)
