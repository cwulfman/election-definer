import lxml.etree

import pytest

from tests.conftest import (
    Paths, load_xml_documents, load_xslt_transform, load_xmlschema_schema
)

XSD_FILE = Paths.DATA / "nist-edf-v2_schema.xsd"
XSLT_FILE = Paths.SOURCES / "ercdf.xsl"


def test_validate_transformed_examples():
    """Test that transformed examples are valid under the NIST EDF schema."""
    xsd_schema = load_xmlschema_schema(XSD_FILE)
    xslt_transform = load_xslt_transform(XSLT_FILE)
    input_documents = load_xml_documents(Paths.INPUTS, "*.in.xml")
    for input_document in input_documents:
        output_document = xslt_transform(input_document).getroot()
        assert xsd_schema.validate(output_document)
