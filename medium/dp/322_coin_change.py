# https://leetcode.com/problems/coin-change/

# Time Complexity - O(Amount * no_of_coins)
# Space Complexity - (Amount)

##### Top-Down Approach #######################################################

INF = float('inf')

def coin_change(coins, amount, dp):
    if amount < 0:
        return -1
    elif amount == 0:
        return 0 # we have reached to the end of the path here

    if dp[amount] != 0: # we have solved this problem...use it.
        return dp[amount]

    min_count = INF
    for coin in coins:
        res = coin_change(coins, amount - coin, dp)
        if res >= 0 and res < min_count:
            min_count = res + 1

    dp[amount] = -1 if min_count == INF else min_count

    return dp[amount]


class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if not coins or amount < -1:
            return -1

        dp = [0] * (amount+1)
        return coin_change(coins, amount, dp)

##### Bottom-Up Approach #######################################################

# class Solution:
#     def coinChange(self, coins, amount):
#         if amount == 0:
#             return 0
#         if not coins or amount < -1:
#             return -1

#         dp = [-1] * (amount + 1)
#         dp[0] = 0
#         for i in range(1, amount+1):
#             items = [dp[i-coin] + 1 for coin in coins if i - coin >= 0 and dp[i-coin] != -1]
#             if items:
#                 dp[i] = min(items)
#             else:
#                 dp[i] = -1

#         return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    assert solution.coinChange([186],186) == 1
    assert solution.coinChange([1],0) == 0
    assert solution.coinChange([2],1) == -1
    assert solution.coinChange([1],2) == 2
    assert solution.coinChange([],100) == -1
    assert solution.coinChange([1], -2) == -1
    assert solution.coinChange([1,2,5],11) == 3
    assert solution.coinChange([2],3) == -1
    assert solution.coinChange([1,5,10,25],49) == 7
    assert solution.coinChange([186,419,83,408], 6249) == 20
    print('done')
