# election-definer
A schema for using a simplified format to define an election, and an XSL stylesheet for transforming that file into a valid NIST 1500-100 ElectionReport.

## Defining an election
Use your preferred XML-aware editor to create a file.  Link it to electiondefinition.rnc for validation.

## Generating an ElectionReport
Use your preferred XSLT processor to run a transform with ercdf.xsl.  For example:

```xsltproc ercdf.xsl examples/partisan-primary.xml -o primary1.xml```

