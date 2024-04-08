#!/usr/bin/python3
"""
Module: 0-nqueens.py

Solve the queens problem
"""


import sys


def is_left(oars, row, col):
    """
    check is the left is safe
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def print_sol(board):
    """
    Print the solution
    """
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()


def solve_problem(board, col):
    """
    solve the problem
    """
    if col >= N:
        print_sol(board)
        return True

    res = False
    for i in range(N):
        if is_left(board, i, col):
            board[i][col] = 1
            res = solve_problem(board, col + 1) or res
            board[i][col] = 0
    return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solve_problem(board, 0)
