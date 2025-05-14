#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers.
Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity
(hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm:
O(log(n)), O(n), O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list
"""

def find_peak(list_of_integers):
    """finds the peak of a list"""
    peak = 0
    if len(list_of_integers) < 3:
        return None
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] > list_of_integers[i - 1]
        and list_of_integers[i] > list_of_integers[i + 1]:
            peak += list_of_integers[i]

    return peak
