#!/usr/bin/python3
def search_replace(my_list, search, replace):
    solution = list(my_list)
    for w in range(len(solution)):
        if solution[w] == search:
            solution[w] = replace
    return solution
