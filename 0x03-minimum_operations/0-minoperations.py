#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    if n <= 1:
        return (0)

    num_op = 0
    while n > 1:
        if n % 2 == 0:
            num_op += 2
            n /= 2
        else:
            num_op += 1
            n -= 1

    return(num_op)
