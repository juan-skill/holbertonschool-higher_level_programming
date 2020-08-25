#!/usr/bin/python3
""" fetches an URL using request package
"""


import requests


def fetch(url=""):
    """ fetch an URL """
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == '__main__':
    fetch("https://intranet.hbtn.io/status")
