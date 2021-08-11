from pathlib import Path

import lxml.etree as etree

import pytest


# --- Paths

# Hardcoded. Better to use an environment variable, or get it from version control.
_HERE = Path(__file__)
# Assumes we are in 'test/py/tests'
_ROOT_PATH = (_HERE.parent / Path("../../..")).resolve()


# Path constants
class Paths:

    ROOT = _ROOT_PATH
    SOURCES = ROOT
    DATA = ROOT / "test" / "data"
    INPUTS = DATA
    OUTPUTS = DATA


# --- Utility functions

def load_xml_document(input_file):
    """Load an XML document from a file."""
    with input_file.open("rb") as file:
        text = file.read()
    xml = etree.XML(text)
    return xml


def load_xml_documents(input_path, file_pattern):
    """Load a sequence of XML documents from a set of files."""
    for file in sorted(input_path.glob(file_pattern)):
        xml = load_xml_document(file)
        yield xml


def load_xslt_transform(input_file):
    """Load an XSLT transform from a file."""
    with input_file.open("rb") as file:
        text = file.read()
    xml = etree.XML(text)
    xslt = etree.XSLT(xml)
    return xslt


def load_xmlschema_schema(input_file):
    """Load an XML Schema schema from a file,"""
    with input_file.open("rb") as file:
        text = file.read()
    xml = etree.XML(text)
    xsd = etree.XMLSchema(xml)
    return xsd


def load_relaxng_schema(input_file):
    """Load a RelaxNG schema from a file,"""
    with input_file.open("rb") as file:
        text = file.read()
    xml = etree.XML(text)
    rng = etree.RelaxNG(xml)
    return rng


def load_relaxng_compact_schema(input_file):
    """Load a RelaxNG compact schema from a file,"""
    with input_file.open("rb") as file:
        text = file.read()
    rng = etree.RelaxNG.from_rnc_string(text)
    return rng
