#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_1 = []
    for d in my_list:
        if d % 2 == 0:
            new_1.append(True)
        else:
            new_1.append(False)
    return new_1
