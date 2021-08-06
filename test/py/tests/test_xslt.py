import re

import lxml.etree

import pytest

from tests.conftest import (
    Paths, load_xml_documents, load_xslt_transform
)


XSLT_FILE = Paths.SOURCES / "ercdf.xsl"


@pytest.fixture(params = load_xml_documents(Paths.INPUTS, "*_in.xml"))
def xml_input_document(request):
    document = request.param
    return document


@pytest.fixture(params = load_xml_documents(Paths.OUTPUTS, "*_out.xml"))
def xml_output_document(request):
    document = request.param
    return document


@pytest.fixture(params = [XSLT_FILE])
def xslt_transform(request):
    file = request.param
    transform = load_xslt_transform(file)
    return transform


def test_transform_examples(xslt_transform, xml_input_document, xml_output_document):
    """Test that XSLT transform turns example XML files into files valid by the EDF schema."""
    actual = xslt_transform(xml_input_document).getroot()
    expected = lxml.etree.tostring(xml_output_document, pretty_print = True)
    actual = lxml.etree.tostring(actual, pretty_print = True)
    # Mangle IDs created with XSLT 'generate-id' so tests can pass.
    # Doing a full element-wise comparison is a lot of work for little benefit here.
    expected = re.sub(b"idm[0-9]+", b"GENERATED", expected)
    actual = re.sub(b"idm[0-9]+", b"GENERATED", actual)
    assert actual == expected
