#!/usr/bin/python3


def roman_to_int(roman_string):

    if isinstance(roman_string, str) is True and roman_string != None:

        number = 0
        str_roman = roman_string + ' '

        i = 0
        while (i < len(str_roman)):

            if str_roman[i] == 'I':
                if str_roman[i + 1] == 'V' or str_roman[i + 1] == 'X':
                    number -= 1
                else:
                    number += 1

            elif str_roman[i] == 'V':
                    number += 5

            elif str_roman[i] == 'X':
                if str_roman[i + 1] == 'L' or str_roman[i + 1] == 'C':
                    number -= 10
                else:
                    number += 10

            elif str_roman[i] == 'L':
                number += 50

            elif str_roman[i] == 'C':
                if str_roman[i + 1] == 'D' or str_roman[i + 1] == 'M':
                    number -= 100
                else:
                    number += 100

            elif str_roman[i] == 'D':
                number += 500

            elif str_roman[i] == 'M':
                number += 1000

            i += 1
        return number
    else:
        return 0
