#!/usr/bin/python3
"""
Minimum Operations
video guia: https://www.youtube.com/watch?v=03ZepmoVJGI&ab_channel=TECHDOSE
"""

"""V1
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
"""

def minOperations(n):
    if n <= 1:
        return (0)

    num_op = 0
    cont_op = 2
    while n > 1:
        if n % cont_op == 0:
            num_op += cont_op
            n /= cont_op
        else:
            cont_op += 1

    return(num_op)
