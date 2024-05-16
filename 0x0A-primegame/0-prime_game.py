#!/usr/bin/python3
"""
Module: 0-prime_game
Prime game
"""


def isWinner(x, nums):
    """
    This function takes turns between Ben and maria to prick prime numners.
    They take turns choosing a prime number from the set,
    and removing that number and its multiples from the set.
    The player that cannot make a move loses the game.

    x: the number of rounds
    nums: an array of n
    Return: name of the player that won the most rounds

    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task maria_wins = 0
    """
    ben_wins = 0
    maria_wins = 0

    max_number = max(nums)
    primes = generate_primes(max_number)

    for n in nums:
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
    This function generates prime numbers up to a given number
    using Sieve of Eratosthenes
    """
    primes = []
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5)+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes
