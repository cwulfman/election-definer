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


def test_transform_examples():
    """Test that XSLT transform turns example XML files into files valid by the EDF schema."""
    xslt_file = _XSLT_FILE
    input_path = _INPUTS_PATH
    expected_path = _EXPECTED_PATH
    # Load transform
    with xslt_file.open("rb") as file:
        text = file.read()
    xml = lxml.etree.XML(text)
    xslt = lxml.etree.XSLT(xml)
    # Load sources
    xml_files = sorted(input_path.glob("*.in.xml"))
    # Load expected results
    edf_files = sorted(expected_path.glob("*.out.xml"))
    for xml_file, edf_file in zip(xml_files, edf_files):
        with xml_file.open("rb") as file:
            text = file.read()
        input_ = lxml.etree.XML(text)
        with edf_file.open("rb") as file:
            text = file.read()
        expected = lxml.etree.XML(text)
        actual = xslt(input_).getroot()
        assert lxml.etree.tostring(actual) == lxml.etree.tostring(expected)
