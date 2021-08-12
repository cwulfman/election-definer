# Testing the election definer

## Setup

Tests are run using PyTest.

To install it set up virtual environment and install the requirements:

```
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r tools/requirements.txt
```

## Running Tests

To run all tests from the root of the project:

```
    $ pytest
```

## Test Directory Structure

Sources for tests are in `test/<language>`, to allow tests to be written in
more than one language to accommodate particular tools.

- `test/py/`: Unit tests in Pytest.

Data is stored independently from the tests in `test/data`. Further
sub-directories should be added as needed.

Tests are named as follows:

```
    test_{description}_{in,out}.{format}
```

- `{description}` identifies the test. PyTest will use these to print useful
  error messages. It allows running a subset of tests, so grouping tests by name
  is useful
- `{in,out}` pairs inputs with expected outputs.

## Notes

### Test files copied from examples

Test files are duplicates of the examples, for a couple of reasons:

- Test file names follow the naming convention that the tests depend on.
- Allows keeping older test cases around even if the examples change.

### Comparing XML elements in tests

- Comparisons of XML trees are done with strings. LXML doesn't provide a single 
  element-wise comparison and writing one for these tests is work for no real benefit.
    - **Note**: LXML guarantees that attributes will be printed in sorted order!
      No such guarantee is made by XML or by other XML processing libraries.
      Again, cross that bridge if we come to it, otherwise it's good enough.

### Mangling ObjectIDs

- The XSL stylesheet generates `ObjectId`s using XSLT's `generate-id` function.
  The generated IDs don't match the originals making a straight up string comparison
  fail. Mangling the strings is the simplest solution. If this breaks further tests
  look into alternate solutions.
