#!/usr/bin/python3
""" display the body of the response or status code """

from urllib import request, error
from sys import argv


def fetch(url=""):
    """ fetchs an URL """
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    fetch(argv[1])
