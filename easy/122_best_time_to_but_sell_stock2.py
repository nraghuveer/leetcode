# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        l = len(prices) - 1
        i = 0
        profit = 0

        while i < l:

            while i < l and prices[i+1] <= prices[i]:
                i += 1
            buy = prices[i]

            while i < l and prices[i+1] > prices[i]:
                i += 1
            sell = prices[i]

            profit += sell - buy

        return profit

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([7,1,5,3,6,4]) == 7
    assert solution.maxProfit([1,2,3,4,5]) == 4
    print('done')
