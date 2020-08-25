#!/usr/bin/python3
""" API Github """

from requests import get
from sys import argv


if __name__ == '__main__':

    try:
        url = 'https://api.github.com/user'
        username = argv[1]
        passwd = argv[2]

        response = get(url, auth=(username, passwd))
        data_json = response.json()

        print(data_json.get('id'))
    except Exception:
        print("None")
