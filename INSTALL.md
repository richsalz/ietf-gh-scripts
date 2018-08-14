
These are python programs; they use PyGitHub which is a Python module
(library) that provides a Python interface to the GitHub API.
The home of PyGitHub is https://github.com/PyGithub/PyGithub

The README says that the simplest way to install PyGithub is to do

    pip install pygithub

My machine did not have pip, so I looked at
https://pip.readthedocs.io/en/stable/installing/ and did this:

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python get-pip.py 
    sudo pip install pygithub

I am a trusting fellow.  You might want to review get-pip before running it.

OR, you can clone and install PyGitHub yourself, or make it a submodule
of this repo, or probably something else.
