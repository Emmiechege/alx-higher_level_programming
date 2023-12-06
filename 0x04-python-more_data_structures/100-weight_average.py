#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    tt_score = 0
    tt_weight = 0
    for score, weight in my_list:
        tt_score = tt_score + (score * weight)
        tt_weight = tt_weight + weight
    if tt_weight == 0:
        return 0
    average = tt_score / tt_weight
    return average
