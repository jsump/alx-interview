#!/usr/bin/python3
"""
Module: 0-pascal_triangle
This module contans a function that prints out Pascal's triangle
"""


def pascal_triangle(n):
    """
    This function prints out Pascal's triangle

    n can always be an integer
    Return an empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
