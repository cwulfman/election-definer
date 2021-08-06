import lxml.etree

import pytest

from tests.conftest import (
    Paths, load_xml_documents, load_xslt_transform, load_relaxng_schema
)


RNG_FILE = Paths.DATA / "electiondefinition.rng"


@pytest.fixture(params = load_xml_documents(Paths.INPUTS, "*_in.xml"))
def xml_input_document(request):
    document = request.param
    return document


@pytest.fixture
def rng_schema():
    file = RNG_FILE
    schema = load_relaxng_schema(file)
    return schema


def test_validate_election_definitions(rng_schema, xml_input_document):
    """Test that simplified election definitions validate under the RNG schema."""
    assert rng_schema.validate(xml_input_document)
