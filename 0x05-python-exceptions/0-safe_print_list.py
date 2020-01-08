#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    if my_list is None or my_list == [] or x == 0:
        print("")
        return 0

    i = 0
    while x > 0:

        try:
            print(my_list[i], end='')
            i += 1
        except IndexError:
            break
        x -= 1

    print("")
    return i
