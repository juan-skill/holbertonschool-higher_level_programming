#!/usr/bin/python3
def remove_char_at(str, n):
    n_str = ""
    for i in range(0, len(str)):
        if (i != n):
            n_str += str[i]
        else:
            continue
    return(n_str)
