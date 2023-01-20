#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    if n <= 1:
        return (0)
    num_H = 1
    num_op = 1
    while num_H != n:
        if num_H * 2 == n:
            num_H *= 2
            num_op += 2
        elif num_H * 3 == n:
            num_H *= 3
            num_op += 3
        else:
            num_H += 1
            num_op += 1

    return(num_op)
