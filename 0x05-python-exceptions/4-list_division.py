#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_lenght):

    new_list = []

    for i in range(list_lenght):

        value = 1
        string = ""

        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            string = 'division by 0\n'
            value = 0
        except IndexError:
            string = 'out of range\n'
            value = 0
        except TypeError:
            string = 'wrong type\n'
            value = 0
        finally:
            new_list.append(value)

        print('{:s}'.format(string), end='') if value != 1 else None

    return new_list
