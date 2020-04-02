
# Installing Dependencies

These are python 3 programs with a couple dependencies. To install the
dependencies, first make sure you have
[`pip`](https://pip.readthedocs.io/en/stable/installing/) and then run:

  python3 -m pip install -r requirements.txt

# Installing tools for i-d-template

The i-d-template repository supports drafts written in XML or markdown.
For full details see
[setup notes](https://github.com/martinthomson/i-d-template/blob/master/doc/SETUP.md).

For XML drafts, you need xml2rfc which is written in Python.
You might also need development versions of libxml and libxslt.

For Markdown, you need kramdown-rfc2629, written in Ruby, or mmark, written in
Go.

Good luck with all that.  See the SETUP link for useful info.
