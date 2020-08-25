#!/usr/bin/python3
""" sends a request and prints a header
"""

from sys import argv
from requests import get


def fetch(url=""):
    """ fetches an URL """
    try:
        response = get(url)
        return response.headers
    except Exception:
        pass


if __name__ == '__main__':
    headers = fetch(argv[1])
    print(headers['X-request-Id'])
