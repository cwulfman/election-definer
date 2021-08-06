import lxml.etree

import pytest

from tests.conftest import (
    Paths, load_xml_documents, load_xslt_transform, load_relaxng_schema
)


RNG_FILE = Paths.DATA / "electiondefinition.rng"


def test_validate_election_definitions():
    """Test that simplified election definitions validate under the RNG schema."""
    rng_schema = load_relaxng_schema(RNG_FILE)
    input_documents = load_xml_documents(Paths.INPUTS, "*.in.xml")
    for input_document in input_documents:
        assert rng_schema.validate(input_document)
