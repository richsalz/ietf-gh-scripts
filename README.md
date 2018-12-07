# ietf-gh-scripts
Scripts to create GH repo's for IETF WG's

The IETF had a couple of WG chair sessions on this, a BoF,
[an I-D](https://datatracker.ietf.org/doc/draft-cooper-wugh-github-wg-configuration/),
and most recently a draft charter was posted on
[IETF and GitHub](https://www.ietf.org/mailman/listinfo/Ietf-and-github).

Martin Thomson has some very nice scripts to manage IETF documents via
GitHub. He's talked about it a couple of times, most recently at the
WGCHAIRS lunch at IETF 102. At that time, I asked about tools to create
the infrastructure -- GitHub organization, repositories for the drafts,
and so on -- and therefore volunteered to make said tools.

In the month or so afterwards, there was some useful discussion on the
WGCHAIRS mailing list and requirements were fleshed out. This repository is
the result. It's written in Python and uses the awesome Github Python API
bindings; see BUILD.md for details.

For example, if SLOW is a new IETF working group with a bad-protocol draft,
this creates a GitHub ietf-wg-slow organization, some groups, and a repository
draft-slow-bad-protocol to hold the draft, common labels for issues,
integration with Martin's tools, and so on.

The two main scripts are:

- mk-ietf-wg Creates an Organization for a working group
- mk-ietf-draft Creates a repository within an existing org for an I-D

If you're not comfortable with building and running these tools, and just want
to get things set up so that you can use GitHub, that's okay.  Just ask
someone who is familiar to run the tools for you (and remind them to remove
themselves from the owner group afterwards).

Look at the issues list to see what's missing.  Make pull requests. :)

