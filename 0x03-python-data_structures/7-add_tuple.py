#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la = len(tuple_a)
    lb = len(tuple_b)
    if la == 0 and lb == 0:
        return(0, 0)
    elif la == 0 and lb >= 2:
        return(tuple_b[0], tuple_b[1])
    elif la == 1 and lb == 0:
        return(tuple_a[0], 0)
    elif la == 0 and lb == 1:
        return(tuple_b[0], 0)
    elif la == 1 and lb == 1:
        return(tuple_a[0] + tuple_b[0], 0)
    elif la >= 2 and lb == 0:
        return(tuple_a[0], tuple_a[1])
    elif la >= 2 and lb == 1:
        e1 = tuple_a[0] + tuple_b[0]
        e2 = tuple_a[1] + 0
        return(e1, e2)
    elif la == 1 and lb >= 2:
        e1 = tuple_a[0] + tuple_b[0]
        e2 = 0 + tuple_b[1]
        return(e1, e2)
    else:
        e1 = tuple_a[0] + tuple_b[0]
        e2 = tuple_a[1] + tuple_b[1]
        return(e1, e2)
