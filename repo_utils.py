"""Utilities to help initialize repositories."""

import os
import os.path
import subprocess
from typing import Dict


TEMPLATE_DIR = os.path.abspath(os.path.dirname(__file__))


def contributing(*, wgname: str) -> str:
    """Returns the contents of a good CONTRIBUTING.md."""
    text = open(os.path.join(TEMPLATE_DIR, "contributing.txt")).read()
    return text % {"WGNAME": wgname}


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
