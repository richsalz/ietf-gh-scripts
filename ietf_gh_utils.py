#! /usr/bin/env python3
"""Some utilities for the IETF GitHub scripts.
"""

# The API is not consistent; sometimes objects are evaluated lazily, and
# sometimes it throws an exception immediately.  That's why the routines here
# look different.

from github import Github

def verify_users(g, user):
    """Verify a |user| or all names in the collection |user| as being valid
    Github users."""
    if isinstance(user, str):
        user = [ user ]
    for u in user:
        try:
            g.get_user(u)
        except:
            raise SystemExit('User "%s" does not exist"' % (u,))
    return 1

def add_gh_auth_arguments(parser):
    """Add arguments needed for logging into Github to the
    argparse.ArgumentParser."""
    group = parser.add_argument_group('Github Auth')
    group.add_argument('--user', '-u', metavar='GH_ID', required=True,
                       help="Github username")
    pw_or_token = group.add_mutually_exclusive_group(required=True)
    pw_or_token.add_argument('--passwd', '-p',
                             help="Github password, " +
                             "if the user doesn't have 2FA enabled")
    pw_or_token.add_argument('--token', '-t',
                             help="Github access token with the public_repo scope: " +
                             "https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line")

def gh_login(args):
    """Login to Github  |args| is the result of parsing command-line arguments
    with the parser passed to add_gh_auth_arguments().
    If both are omitted, username and password will be prompted-for.  Returns
    the handle and the username"""
    if args.token is not None:
        g = Github(args.token)
    else:
        if not args.user:
            pass
        if not args.passwd:
            pass
        g = Github(args.user, args.passwd)
    try:
        g.get_user(args.user)
    except:
        raise SystemExit('Github Login failed')
    return g, args.user

def org_exists(g, org):
    """See if |org| organization exists."""
    try:
        g.get_organization(org)
    except:
        return None
    return True

def repo_exists(g, repo):
    """See if repository |repo| exists."""
    try:
        g.get_repo(repo).owner
    except:
        return None
    return True

def fix_wg_name(wgname):
    """Check no non-alphanumerics and convert to lowercase."""
    wgname = wgname.lower()
    if wgname.isalnum():
        return wgname
    raise SystemExit('Non-alphanumeric in WG name: "%s"' % (wgname,))
    return wgname
