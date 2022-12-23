#!/usr/bin/python3
"""
    Pascal Triangle
"""

def pascal_triangle(n):
    """
    n = no of rows
    returns: list of integers implemeting pascle tringle
    """
    for i in range(n+1):
        for j in range(n-i):
            print(' ', end='')

        body = 1
        for j in range(1, i+1):
            print(body, ' ', sep='', end='')
            body = body * (i - j) // j
        print()
