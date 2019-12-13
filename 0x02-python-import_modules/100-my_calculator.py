#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
from sys import exit


def main():
    length = len(argv)

    if length != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    else:
        num1 = int(argv[1])
        num2 = int(argv[3])
        sign = argv[2]

        if sign == '+':
            print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
        elif sign == '-':
            print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
        elif sign == '*':
            print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
        elif sign == '/':
            print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    main()
