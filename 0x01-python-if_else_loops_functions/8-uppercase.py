#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 90:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
