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
    if not nums or x < 1:
        return None

    def sieve(n):
        """
        Generate list of prime numbers up to n using
        the Sieve of Eratosthenes.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0] = is_prime[1] = False
        primes = []
        for p in range(n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes

    max_n = max(nums)
    primes = sieve(max_n)

    def calculate_winner(n):
        """Calculate the winner for a single round."""
        if n < 2:
            return "Ben"

        primes_in_game = [p for p in primes if p <= n]
        moves = 0
        while primes_in_game:
            prime = primes_in_game[0]
            primes_in_game = [p for p in primes_in_game if p % prime != 0]
            moves += 1

        if moves % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = calculate_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
