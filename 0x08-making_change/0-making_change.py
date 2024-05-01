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

    # Dictionary to store fewest number of coins for each amnt
    min_coins = {0: 0}

    for coin in coins:
        for amnt in range(coin, total + 1):
            if amnt - coin in min_coins:
                min_coins[amnt] = min(min_coins.get(
                    amnt, float('inf')
                    ), min_coins[amnt - coin] + 1)

    return min_coins.get(total, -1)
