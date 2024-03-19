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

    minNumOfOp = [0] * (n + 1)

    for i in range(2, n + 1):
        minNumOfOp[i] = float('inf')
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                minNumOfOp = min(minNumOfOp[i], minNumOfOp[j] + i // j)

                minNumOfOp = min(minNumOfOp[i], minNumOfOp[i //j] + j)

    return minNumOfOp if minNumOfOp[n] != float('inf') else 0
