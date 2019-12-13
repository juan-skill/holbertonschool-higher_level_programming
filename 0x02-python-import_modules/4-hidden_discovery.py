#!/usr/bin/python3
import hidden_4


def main():
    i = 0

    for i in range(0, len(dir(hidden_4))):
        if "__" not in dir(hidden_4)[i]:
            print(dir(hidden_4)[i])


if __name__ == "__main__":
    main()
