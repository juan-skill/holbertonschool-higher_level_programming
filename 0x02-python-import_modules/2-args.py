#!/usr/bin/python3
from sys import argv


def main():
    number = len(argv)
    pos = ""

    if number == 1:
        str = 's.\n'
    elif number == 2:
        str = ':\n'
    elif number > 2:
        str = 's:\n'

    print("{} argument".format(number - 1), end=str)
    for i in range(1, number):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
