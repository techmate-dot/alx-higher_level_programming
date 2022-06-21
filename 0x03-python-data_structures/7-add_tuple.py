#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    la = len(tuple_a)
    lb = len(tuple_b)
    new_tup = ()
    if la < lb:
        tuple_a + (0, )
    elif la > lb:
        tuple_b + (0, )

    for i in range(len(tuple_a)):
        new_tup += (tuple_a[i] + tuple_b[i], )
    return new_tup
