import re

import lxml.etree

import pytest

from tests.conftest import (
    Paths, load_xml_documents, load_xslt_transform
)


XSLT_FILE = Paths.SOURCES / "ercdf.xsl"


def test_transform_examples():
    """Test that XSLT transform turns example XML files into files valid by the EDF schema."""
    xslt_transform = load_xslt_transform(XSLT_FILE)
    input_files = load_xml_documents(Paths.INPUTS, "*.in.xml")
    output_files = load_xml_documents(Paths.OUTPUTS, "*.out.xml")
    for input_doc, output_doc in zip(input_files, output_files):
        actual = xslt_transform(input_doc).getroot()
        expected = lxml.etree.tostring(output_doc, pretty_print = True)
        actual = lxml.etree.tostring(actual, pretty_print = True)
        # Mangle IDs so that the text comparison will work.
        expected = re.sub(b"idm[0-9]+", b"GENERATED", expected)
        actual = re.sub(b"idm[0-9]+", b"GENERATED", actual)
        assert actual == expected
