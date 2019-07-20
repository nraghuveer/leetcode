# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        k = 2

        l = len(prices)
        dp = [[0 for i in range(l)] for j in range(k+1)]

        for i in range(1,k+1):
            max_diff = dp[i][0] - prices[0]
            for j in range(1,l):
                dp[i][j] = max(dp[i][j-1],
                               prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j] - prices[j])

        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([2,5,7,1,4,3,1,3]) == 8
    assert solution.maxProfit([3,3,5,0,0,3,1,4]) == 6
    assert solution.maxProfit([1,2,3,4,5]) == 4
    print('done')



