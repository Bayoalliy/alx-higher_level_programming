#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lst = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            lst.append(i)
    if lst:
        for x in lst:
            del a_dictionary[x]
    return(a_dictionary)
