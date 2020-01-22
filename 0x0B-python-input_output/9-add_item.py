#!/usr/bin/python3
"""this script adds all arguments to a Python list and saves them in file"""


from sys import argv
"""sys.argv is a list in Python"""

save = __import__('7-save_to_json_file').save_to_json_file
""" dumps module json decodes the json data."""

load = __import__('8-load_from_json_file').load_from_json_file
""" loads module json obtains a Python object list """


filename = "add_item.json"

try:
    my_list = load(filename)
    save(my_list + argv[1:], filename)

except Exception:
    save(argv[1:], filename)
