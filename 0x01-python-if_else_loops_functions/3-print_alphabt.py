#!/usr/bin/python3

i = 0
while(i < 26):
    if (chr(i + 97) != 'e' and chr(i + 97) != 'q'):
        print("{:c}".format(i + 97), end="")
    i += 1
