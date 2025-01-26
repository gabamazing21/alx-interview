#!/usr/bin/python3
"""
counting coins
"""


def makeChange(coins, total):
    if total == 0:
        return 0
    if total < 0:
        return -1

    # Initialize a list to store minimum coins
    # needed for each amount
    # we use total + 1 as a "infinity" value r
    # epresenting impossible combination
    dp = [total + 1] * (total + 1)

    # 0 coins needed to make 0 amount
    dp[0] = 0

    for amount in range(1, total + 1):
        # try each coin denomination
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
