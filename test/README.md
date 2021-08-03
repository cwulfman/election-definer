# Testing the election definer.

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

