#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculations(a, b)
    if a < b:
        c = add(a, b)
        for m in range(4, 6):
            c = add(c, m)
        return (c)
    else:
        return(sub(a, b))
