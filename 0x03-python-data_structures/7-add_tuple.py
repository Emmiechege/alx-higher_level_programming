#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    e = list(tuple_a)   # convert tuple to list
    f = list(tuple_b)

    while len(e) < 2:
        e.append(0)
    while len(f) < 2:
        f.append(0)

    e = e[:2]   # two elements per tuple
    f = f[:2]
    return (e[0] + f[0], e[1] + f[1])
