#!/usr/bin/python3
""" Use Github API to display list 10 commits
(from the most recent to oldest) of the repository “”
by the user"""


from requests import get, exceptions
from sys import argv


def fetch(url=""):
    """ fetches an URL """
    try:
        req = get(url)
        req.raise_for_status()
        return req.json()

    except exceptions.RequestException as e:
        print(e.code)


def print_json(data_json):
    """ print json resources """

    try:
        for commit in data_json[:10]:
            sha = commit['sha']
            name = commit['commit']['author']['name']
            print("{}: {}".format(sha, name))

    except Exception as e:
        print(str(e))


if __name__ == "__main__":

    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    data_json = fetch(url)
    print_json(data_json)
