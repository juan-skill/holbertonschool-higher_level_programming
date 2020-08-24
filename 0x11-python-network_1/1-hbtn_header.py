#!/usr/bin/python3
""" display a response header
"""
from urllib import request
from sys import argv


def fetch(url=""):
    """ fetch a URL """
    with request.urlopen(url) as response:
        return response.info()


if __name__ == '__main__':
    headers = fetch(argv[1])
    print(headers["X-Request-Id"])
