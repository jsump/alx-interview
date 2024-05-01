#!/usr/bin/python3
"""
Module: 0-making_change.py

This module contains a functoin that changes the value of coins
"""


def makeChange(coins, total):
    """
    This method takes a pile of coins of different values,
    determines the fewest number of coins needed to meet
    a given amount total
    """
    if total <= 0:
        return 0

    # List creation to store fewest number of coins for each amnt
    la = [float('inf')] * (total + 1)
    la[0] = 0

    for coin in coins:
        for amnt in range(coin, total + 1):
            la[amnt] = min(la[amnt], la[amnt - coin] + 1)

    if la[total] == float('inf'):
        return -1
    else:
        return la[total]
