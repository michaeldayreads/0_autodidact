"""Script to create closed, locked issues for repos transferred to GitHub."""

import requests
import json
import tos
import time

first_issue = 25
last_issue = 220
owner = 'foo'
repo = 'bar'

def api_request(resource, data, method):
    base = 'https://api.github.com'
    auth_data = tos.github()
    auth = (auth_data['user'], auth_data['token'])
    url = base + resource
    print "Attempting %s to %s" % (method, url)
    if method == "post":
        r = requests.post(url, auth=auth, data=json.dumps(data))
    elif method == "patch":
        r = requests.patch(url, auth=auth, data=json.dumps(data))
    elif method == "put":
        r = requests.put(url, auth=auth)
    else:
        print "[warning] no method provided, no call made"
    print r.status_code

def create_issue(owner, repo):
    data = {
        "title": "Internal issue %i" % issue_number,
        "body": "This is a placeholder for a resolved issue that pre-dates GitHub development."
    }
    resource = "/repos/%s/%s/issues" % (owner, repo)
    api_request(resource, data, "post")


def close_issue(owner, repo, issue_number):
    data = {"state": "closed"}
    resource = "/repos/%s/%s/issues/%i" % (owner, repo, issue_number)
    api_request(resource, data, "patch")


def lock_issue(owner, repo, issue_number):
    resource = "/repos/%s/%s/issues/%i/lock" % (owner, repo, issue_number)
    data = ""
    api_request(resource, data, "put")


for issue_number in range(first_issue, last_issue+1):
    create_issue(owner, repo)
    time.sleep(.25)
    close_issue(owner, repo, issue_number)
    time.sleep(.25)
    lock_issue(owner, repo, issue_number)
    time.sleep(.25)
