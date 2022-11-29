#!/usr/bin/python3
for i in range(1, 100):
    if i >= 10 and i % 10 == 0:
        continue
    if i >= 20 and i % 10 == 1:
        continue
    if i >= 30 and i % 10 == 2:
        continue
    if i >= 40 and i % 10 == 3:
        continue
    if i >= 50 and i % 10 == 4:
        continue
    if i >= 60 and i % 10 == 5:
        continue
    if i >= 70 and i % 10 == 6:
        continue
    if i >= 80 and i % 10 == 7:
        continue
    if i >= 90 and i % 10 == 8:
        continue
    if i % 11 == 0:
        continue
    if i == 1:
        print("{:0>2d}".format(i), end="")
    else:
        print(", {:0>2d}".format(i), end="")
print("")
