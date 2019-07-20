# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Maximize the profit"""
        if not prices:
            return 0

        max_profit , min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([7,1,5,3,6,4]) == 5
    print('done')