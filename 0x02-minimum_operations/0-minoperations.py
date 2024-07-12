#!/usr/bin/python3
"""
Minimum Operations Module
"""

def minOperations(n):
    """
    Calculates the minimum number of operations needed to get
    exactly n 'H' characters using only copy and paste operations.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if impossible.
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
