#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return("None")
    keys = list(a_dictionary)
    big_key = keys[0]
    for i in a_dictionary:
        if a_dictionary[i] > a_dictionary[big_key]:
            big_key = i
    return (big_key)
