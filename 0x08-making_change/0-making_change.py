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

    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            coin_count += 1
        if total == 0:
            return coin_count

    return -1
