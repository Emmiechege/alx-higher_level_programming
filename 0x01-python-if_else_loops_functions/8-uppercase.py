#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for y in str:
        if ord(y) >= 97 and ord(y) <= 122:
            string_upp = string_upp + chr(ord(y) - 32)
        else:
            string_upp = string_upp + y
    print("{}".format(string_upp))
