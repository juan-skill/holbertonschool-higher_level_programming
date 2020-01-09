#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):

    ret = True
    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError) as msg_error:
        stderr.write('Exception: {}\n'.format(msg_error))
        ret = False

    return (ret)
