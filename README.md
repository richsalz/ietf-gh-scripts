# ietf-gh-scripts
Scripts to create GH repo's for IETF WG's

Martin Thomson has some very nice scripts to manage IETF documents via
GitHub. He's talked about it a couple of times, most recently at the
WGCHAIRS lunch at IETF 102. At that time, I asked about tools to create
the infrastructure -- GitHub organization, repositories for the drafts,
and so on and therefore volunteered to make said tools.

In the month or so afterwards, there was some useful discussion on the
WGCHAIRS mailing list and requirements were fleshed out. This repository
is the result. It's written in Python and uses the awesome Github Python
API bindings; see BUILD.md for details.

- mk-ietf-wg Creates an Organization for a working group
- mk-ietf-draft Creates a repository within an existing org for an I-D

Look at the issues list to see what's missing.  Make pull requests. :)

