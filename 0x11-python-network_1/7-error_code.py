#!/usr/bin/python3
""" Handling Error resquest """


from requests import get
from sys import argv


def fetch(url=""):
    """ fetches an URL """

    try:
        response = get(url)
        response.raise_for_status()
        print(response.text)

    except Exception:
        print("Error code: {}".format(response.status_code))


if __name__ == '__main__':
    fetch(argv[1])
