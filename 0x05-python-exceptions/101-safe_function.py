#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):

    try:
        ret = fct(*args)
    except Exception as msg_eror:
        stderr.write('Exception: {}\n'.format(msg_error))
        return None

    return ret
