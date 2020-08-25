#!/usr/bin/python3
""" sends a POST request """


from requests import post
from sys import argv


def fetch(url="", value=""):
    """ fetches an URL """
    try:
        data = {'email': value}
        response = post(url=url, data=data)
        return response.text
    except Exception:
        pass


if __name__ == '__main__':
    body = fetch(argv[1], argv[2])
    print(body)
