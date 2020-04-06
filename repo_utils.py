"""Utilities to help initialize repositories."""

import os
import os.path
import shutil
import subprocess
import sys
from typing import Dict


TEMPLATE_DIR = os.path.abspath(os.path.dirname(__file__))


def contributing(*, wgname: str) -> str:
    """Returns the contents of a good CONTRIBUTING.md."""
    text = open(os.path.join(TEMPLATE_DIR, "contributing.txt")).read()
    return text % {"WGNAME": wgname}


def initial_draft(*, full_draft_name: str, docname: str, wg: str = None) -> str:
    """Returns an initial I-D for this repository."""
    workgroup = ""
    if wg is not None:
        workgroup = "workgroup: {}\n".format(wg)
    template = """---
docname: {full_draft_name}-latest
title: The {docname} draft
category: exp
{workgroup}
ipr: trust200902

author:
  -
    name: John Doe
    org: Organization
    email: user@example.org

stand_alone: yes
pi: [toc, sortrefs, symrefs]

--- abstract

Content here.

--- middle

# Introduction
"""
    return template.format(**vars())


def check_i_d_tools_are_installed() -> None:
    """Makes sure any non-Python tools needed to build an I-D are installed.

    Call this early in the main script, before causing side-effects like
    creating a Github repository, to reduce the chance the user will have to
    manually undo things because the script failed.
    """
    if shutil.which("kramdown-rfc2629") is None:
        sys.exit("Error: Please install kramdown-rfc2629 as described in " +
                 "https://github.com/martinthomson/i-d-template/blob/master/doc/SETUP.md")


def clone_and_create_initial_commit(*, user: str, repo: str, default_branch: str = "master", initial_files: Dict[str, str]) -> None:
    """Clones the specified repository from Github and creates an initial commit consisting of the |initial_files|.

    Leaves the current directory inside the new checkout.
    """
    subprocess.run(["git", "clone", "git@github.com:{}/{}".format(user, repo)],
                   check=True)
    os.chdir(repo)
    subprocess.run(["git", "checkout", "--orphan", default_branch],
                   check=True)
    for filename, contents in initial_files.items():
        with open(filename, "w") as f:
            f.write(contents)
    subprocess.run(["git", "add"] + list(initial_files.keys()),
                   check=True)
    subprocess.run(["git", "commit", "-m", "Initial docs"],
                   check=True)
    subprocess.run(["git", "push", "--set-upstream", "origin", default_branch],
                   check=True)


def setup_i_d_template() -> None:
    """Sets up martinthomson/i-d-template in the current directory."""
    subprocess.run(["git", "clone", "https://github.com/martinthomson/i-d-template", "lib"],
                   check=True)
    subprocess.run(["make", "-f", "lib/setup.mk"],
                   check=True)
    subprocess.run(["git", "push"],
                   check=True)
