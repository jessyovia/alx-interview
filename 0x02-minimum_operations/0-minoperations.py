#!/usr/bin/python3
"""
Module to calculate the minimum number of operations
needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Calculates the minimum number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): Target number of H characters

    Returns:
        int: Minimum number of operations
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
