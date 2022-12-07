#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ls = sorted(list(a_dictionary))
    for i in ls:
        print("{}: {}".format(i, a_dictionary[i]))
