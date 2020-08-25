#!/usr/bin/python3
""" sends a POST request """


from requests import post
from sys import argv


def fetch(url="", value=""):
    """ fetches an URL """

    try:
        payload = {'q': value}

        response = post(url, payload)
        response.raise_for_status()
        response_json = response.json()
        # print(response.json)

        if len(response_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(response_json['id'], response_json['name']))
    except Exception as e:
        print(str(e))


if __name__ == '__main__':

    url = "http://0.0.0.0:5000/search_user"

    if len(argv[1]) > 1:
        q_argument = argv[1]
    else:
        q_argument = ""

    fetch(url, q_argument)
