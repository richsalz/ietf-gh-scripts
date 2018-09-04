
These are python programs; they use PyGitHub which is a Python module
(library) that provides a Python interface to the GitHub API.
The home of PyGitHub is https://github.com/PyGithub/PyGithub

There are a couple of ways to add PyGithub to your Python library.  These
scripts use a bug-fixed version of master which, as of this writing,
hasn't been released yet.  Assuming no regressions, this method will
always work:

	git clone git@github.com:PyGithub/PyGithub.git PyGithub
	cd PyGithub
	sudo python setup.py install

The PyGithub README says that the simplest way to install is to do:

    pip install pygithub

My machine did not have pip, so I looked at
https://pip.readthedocs.io/en/stable/installing/ and did this:

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python get-pip.py 
    sudo pip install pygithub

You might want to review get-pip before running it; good luck with that.

I am a trusting fellow.

If you have a non-root directory in your PYTHONPATH (ugh, why would you?)
or you're willing to modify the scripts to update that path, you can
do the equivalent of this:

	cd PyGithub
	python seutp.py build
	export PYTHONPATH=...path.../ietf-gh-scripts/PyGithub/build/lib

There are probably other ways to do it, too.
