#!/usr/bin/python3
"""
Minimum Operations
"""
def minOperations(n):
    if n <= 0:
        return (0)
    num_H = 1
    while num_H != n:
        if num_H * 2 == n:
            num_H += 2
        elif num_H * 3 == n:
            num_H += 3
        else:
            num_H += 1

    return(num_H)
