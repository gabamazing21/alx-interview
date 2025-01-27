#!/usr/bin/python3
"""prime interview questions"""


def isWinner(x, nums):
    """
    Determine the winner of multile rounds of
    the prime game between maria and ben.

    Args:

    """
    def get_primes_up_to(n):
        """
        generate a list of prime numbers up to
        n using the sieve of eratoshenes
        """
        if n < 2:
            return [], [False] * (n + 1)

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        primes = [i for i in range(2, n + 1) if is_prime[i]]
        return primes, is_prime

    def play_round(n):
        """
        similate a single round of the
        game with starting number
        """
        if n < 2:
            return False

        primes, is_prime = get_primes_up_to(n)

        removed = [False] * (n + 1)
        maria_turn = True

        while True:
            next_prime = None
            for prime in primes:
                if prime > n:
                    break
                if not any(removed[prime::prime]):
                    next_prime = prime
                    break

            if next_prime is None:
                return not maria_turn

            for i in range(next_prime, n + 1, next_prime):
                removed[i] = True

            maria_turn = not maria_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        if play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
