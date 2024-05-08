#!/usr/bin/python3
"""
Module: 0-island_perimeter.py
This module contains a function that returns the perimeter
of the island descibed in grid
"""


def island_perimeter(grid):
    """
    This function returns the perimetre of the island described in grid

    grid: list of integers:
        - 0: water
        - 1: land
        - Each cell is swuare, side length of 1
        - Cells are connected horizontally and diagonally only
        - grid is rectangular, width and height <= 100
    Grid is completely surrounded by water
    There's only one island or nothing
    Island doesn't have lakes
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    # Iterate through each cell in grid
    for i in range(rows):
        for j in range(cols):
            # check is current cell is land
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell adds 4 to the perimeter

                # Check adjacent cells to subtract shared edges
                # Check if there is land to the top of the current cell
                if i > 0 and grid[i - 1][j] == 1:
                    # Subtract 2 for shared edge
                    perimeter -= 2

                # Check if there is land to the left of the current cell
                if j > 0 and grid[i][j - 1] == 1:
                    # Subtract 2 for shared edge
                    perimeter -= 2
    return perimeter
