#!/usr/bin/python3


def uniq_add(my_list=[]):

    n_list = []
    v_sum = 0

    for i in my_list:
        if i not in n_list:
            n_list.append(i)
            v_sum += i

    return v_sum
