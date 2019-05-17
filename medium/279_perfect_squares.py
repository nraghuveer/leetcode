# https://leetcode.com/problems/perfect-squares/

from math import sqrt, floor

class Solution:
    # def isPerfect(self, value):
    #     """ Checks if the given value is perfect square number """
    #     return (sqrt(value) - float(sqrt(value))) == 0

    # def getPrev(self, value):
    #     """ returns perfect square that is immediate less than the given value """
    #     prev = int(sqrt(value))
    #     return prev ** 2

    def numSquares(self, n: int):
        dp = {} # init the array of size n with max value as n
        dp[0] = 0
        dp[1] = 1
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j*j > i:
                    break

                dp[i] = min(dp.get(i, n), dp.get(i - j*j, n) + 1)
        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    assert solution.numSquares(12) == 3
