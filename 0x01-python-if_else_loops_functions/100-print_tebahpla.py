#!/usr/bin/python3
i = 25
alp = ""
while(i >= 0):
    alp = alp + chr(i + 97) if (i % 2) else alp + chr(i + 65)
    i -= 1
print("{}".format(alp), end='')
