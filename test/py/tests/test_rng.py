import lxml.etree

import pytest

from tests.conftest import Paths


RNG_FILE = Paths.DATA / "electiondefinition.rng"


def test_validate_election_definitions():
    """Test that simplified election definitions validate under the RNG schema."""

    # Load schema
    with RNG_FILE.open("rb") as file:
        text = file.read()
    xml = lxml.etree.XML(text)
    rng = lxml.etree.RelaxNG(xml)

    # Load sources
    xml_files = sorted(Paths.INPUTS.glob("*.in.xml"))
    for xml_file in xml_files:
        with xml_file.open("rb") as file:
            text = file.read()
        input_ = lxml.etree.XML(text)
        assert rng.validate(input_)
