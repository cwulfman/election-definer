import lxml.etree

import pytest

from tests.conftest import (
    Paths, load_xml_documents, load_xslt_transform, load_xmlschema_schema
)

XSD_FILE = Paths.DATA / "nist-edf-v2_schema.xsd"
XSLT_FILE = Paths.SOURCES / "ercdf.xsl"


@pytest.fixture(params = load_xml_documents(Paths.INPUTS, "*_in.xml"))
def xml_input_document(request):
    document = request.param
    return document


@pytest.fixture(params = [XSLT_FILE])
def xslt_transform(request):
    file = request.param
    transform = load_xslt_transform(file)
    return transform


@pytest.fixture
def xsd_schema():
    file = XSD_FILE
    schema = load_xmlschema_schema(file)
    return schema


def test_validate_transformed_examples(xsd_schema, xslt_transform, xml_input_document):
    """Test that transformed examples are valid under the NIST EDF schema."""
    xml_output_document = xslt_transform(xml_input_document).getroot()
    assert xsd_schema.validate(xml_output_document)
