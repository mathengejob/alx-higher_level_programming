#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = []
    for lst in matrix:
        squared = list(map((lambda x: x * x), lst))
        newlist.append(squared)
    return(newlist)
