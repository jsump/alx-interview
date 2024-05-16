#!/usr/bin/python3
"""
Module: 0-prime_game
Prime game
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
    - x: the number of rounds
    - nums: an array of n for each round

    Returns:
    - The name of the player that wins the game.
      If the winner cannot be determined, returns None.
    """

    ben_wins = 0
    maria_wins = 0

    if not nums:
        return None

    for n in nums:
        if is_prime(n):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def is_prime(n):
    """
    Checks if a number is prime.

    Args:
    - n: the number to check

    Returns:
    - True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
