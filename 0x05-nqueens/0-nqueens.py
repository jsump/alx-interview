#!/usr/bin/python3
"""
Module: 0-nqueens.py

This module solves he queens problem in chess
"""


import sys


def is_valid(board, row, col, N):
    """
    This method checks if queen can be in board
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_queen(board, row, N, solutions):
    """
    This method gives the queen solutions on moves to make
    """
    if row == N:
        solutions.append(list(board))
    else:
        for col in range(N):
            if is_valid(board, row, col, N):
                board[row] = col
                solve_queen(board, row + 1, N, solutions)


def nqueens(N):
    """
    This method solves the queens problem
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be greater or equal to 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_queen(board, 0, N, solutions)

    for solution in solutions:
        formatted_solution = [[i, col] for i, col in enumerate(solution)]
        print(formatted_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
