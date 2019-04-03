#! /usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ietf_gh_scripts",
    version="0.1.0",
    author="Rich Salz",
    author_email="rsalz@akamai.com",
    description="Tools to automate IETF/GitHub workflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/richsalz/ietf-gh-scripts",
    scripts=[ "mk-ietf-draft", "mk-ietf-wg", "mk-ind-draft" ],
    packages=setuptools.find_packages(),
    package_data={
        "": [ "*.md", "*.txt", "ietf-logo.jpeg", "LICENSE" ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
