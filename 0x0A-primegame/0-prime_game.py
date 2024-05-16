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

    ben_wins = 0
    maria_wins = 0

    for n in nums:
        # Generate primes using Sieve of Eratosthenes
        primes = generate_primes(n)
        
        # Check if n is 1 or a prime number
        if n == 1 or n in primes:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def generate_primes(n):
    """
    Generates prime numbers up to a given number using Sieve of Eratosthenes.

    Args:
    - n: the upper limit for generating primes

    Returns:
    - A set containing prime numbers up to n
    """

    primes = set()
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5)+1):
        if sieve[p]:
            primes.add(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes
