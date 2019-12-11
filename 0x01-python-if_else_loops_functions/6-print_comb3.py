#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0, 10):
        if j > i and i is not 8:
            print("{}{}".format(i, j), end=', ')
print("89")
