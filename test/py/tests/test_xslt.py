import re

import lxml.etree

import pytest

from tests.conftest import Paths


XSLT_FILE = Paths.SOURCES / "ercdf.xsl"


def test_transform_examples():
    """Test that XSLT transform turns example XML files into files valid by the EDF schema."""

    # Load transform
    with XSLT_FILE.open("rb") as file:
        text = file.read()
    xml = lxml.etree.XML(text)
    xslt = lxml.etree.XSLT(xml)

    # Load sources
    xml_files = sorted(Paths.INPUTS.glob("*.in.xml"))

    # Load expected results
    edf_files = sorted(Paths.OUTPUTS.glob("*.out.xml"))
    for xml_file, edf_file in zip(xml_files, edf_files):
        with xml_file.open("rb") as file:
            text = file.read()
        input_ = lxml.etree.XML(text)
        with edf_file.open("rb") as file:
            text = file.read()
        expected = lxml.etree.XML(text)
        actual = xslt(input_).getroot()
        expected = lxml.etree.tostring(expected, pretty_print = True)
        actual = lxml.etree.tostring(actual, pretty_print = True)
        # Mangle IDs so that the text comparison will work.
        expected = re.sub(b"idm[0-9]+", b"GENERATED", expected)
        actual = re.sub(b"idm[0-9]+", b"GENERATED", actual)
        assert actual == expected
