#!/usr/bin/python3
""" displays body response
"""

from urllib import request


def fetch(url=""):
    """ fetchs a URL """
    try:
        with request.urlopen(url) as response:
            body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

    except Exception as e:
        print(str(e))


if __name__ == "__main__":

    fetch("https://intranet.hbtn.io/status")
