#!/usr/bin/python3
import sys


if __name__ == "__main__":
    list_args = sys.argv[1:]
    total = 0
    for k in list_args:
        total = total + int(k)
    print(total)
