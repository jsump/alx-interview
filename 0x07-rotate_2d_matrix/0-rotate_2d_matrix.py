#!/usr/bin/python3
"""
Module: 0-rotate_2d_matrix.py
Rotate a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    This method rotates a 2d matrix
    does not retuen anything
    assume the 2 dimentions are not empty
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = \
                matrix[i][n - 1 - j], matrix[i][j]
