#! /usr/bin/env python
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

def gh_login(np):
    """Login to Github  |np| is colon-separated name and password, if omitted
    either one will be prompted-for.  Returns the handle and the username"""
    name = None
    passwd = None
    if np is not None:
        name, passwd = np.split(':', 1)
    if not name:
        pass
    if not passwd:
        pass
    g = Github(name, passwd)
    try:
        g.get_user(name)
    except:
        raise SystemExit('Github Login failed')
    return g, name

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
