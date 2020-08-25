#!/usr/bin/python3
""" sent a POST request with email as a parameter
"""

from urllib import request, parse
from sys import argv


def fetch(url="", email=""):
    """ fetch an URL """
    try:
        values = {"email": email}
        data = parse.urlencode(values)
        data_encode = data.encode('utf-8')
        req = request.Request(url, data_encode)

        with request.urlopen(req) as response:
            body = response.read()

        print(body.decode('utf-8'))

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    fetch(argv[1], argv[2])
