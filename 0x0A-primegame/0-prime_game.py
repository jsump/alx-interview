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
    - The name of the player that won the most rounds.
      If the winner cannot be determined, returns None.
    """

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of prime numbers left after Maria and Ben's turns
        primes_left = count_primes_left(n)
        
        # If there are an even number of primes left, Ben wins; otherwise, Maria wins
        if primes_left % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def count_primes_left(n):
    """
    Counts the number of prime numbers left after Maria and Ben's turns.

    Args:
    - n: the number for the current round

    Returns:
    - The count of prime numbers left in the set after Maria and Ben's turns.
    """

    primes_left = 0
    remaining = set(range(2, n + 1))

    while remaining:
        # Maria's turn
        prime = min(remaining)
        primes_left += 1
        remaining -= set(range(prime, n + 1, prime))

        # Check if Ben can make a move
        if not remaining:
            break

        # Ben's turn
        prime = min(remaining)
        remaining -= set(range(prime, n + 1, prime))

    return primes_left
