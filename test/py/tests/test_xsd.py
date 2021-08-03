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

_XSLT_FILE = _SOURCE_PATH / "ercdf.xsl"
_XSD_FILE = _DATA_PATH / "nist-edf-v2_schema.xsd"


def test_validate_transformed_examples():
    """Test that transformed examples are valid under the NIST EDF schema."""
    xsd_file = _XSD_FILE
    xslt_file = _XSLT_FILE
    input_path = _INPUTS_PATH

    # Load transform
    with xslt_file.open("rb") as file:
        text = file.read()
    xml = lxml.etree.XML(text)
    xslt = lxml.etree.XSLT(xml)

    # Load schema
    with xsd_file.open("rb") as file:
        text = file.read()
    xml = lxml.etree.XML(text)
    xsd = lxml.etree.XMLSchema(xml)

    # Load sources
    xml_files = sorted(input_path.glob("*.in.xml"))
    for xml_file in xml_files:
        with xml_file.open("rb") as file:
            text = file.read()
        input_ = lxml.etree.XML(text)
        transformed = xslt(input_).getroot()
        assert xsd.validate(transformed)
