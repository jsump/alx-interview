#!/usr/bin/python3
"""
Module: 0-minoperations.py

This module contatins a function that executes two operations.
"""


def minOperations(n):
    """
    Given that the text editior can only perform two operations
    in this file, this method calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Returns an integer
    If n is impossible to acieve, return 0
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
