import lxml.etree

import pytest

from tests.conftest import Paths


XSD_FILE = Paths.DATA / "nist-edf-v2_schema.xsd"
XSLT_FILE = Paths.SOURCES / "ercdf.xsl"


def test_validate_transformed_examples():
    """Test that transformed examples are valid under the NIST EDF schema."""

    # Load transform
    with XSLT_FILE.open("rb") as file:
        text = file.read()
    xml = lxml.etree.XML(text)
    xslt = lxml.etree.XSLT(xml)

    # Load schema
    with XSD_FILE.open("rb") as file:
        text = file.read()
    xml = lxml.etree.XML(text)
    xsd = lxml.etree.XMLSchema(xml)

    # Load sources
    xml_files = sorted(Paths.INPUTS.glob("*.in.xml"))
    for xml_file in xml_files:
        with xml_file.open("rb") as file:
            text = file.read()
        input_ = lxml.etree.XML(text)
        transformed = xslt(input_).getroot()
        assert xsd.validate(transformed)
