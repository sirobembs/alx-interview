#!/usr/bin/python3
"""Minimum operations
"""
    
def minOperations(n):
    if n <= 0:
        return 0
    operations = 0
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
        operations += 1
        
    return operations