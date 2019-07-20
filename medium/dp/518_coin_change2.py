# https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0

        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(1,amount+1):
                if coin <= i:
                    dp[i] += dp[i-coin]

        return dp[-1]