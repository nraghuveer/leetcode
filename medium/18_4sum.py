# https://leetcode.com/problems/4sum/

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        if n == 0 or n < 4:
            return result

        if n == 4:
            return sorted(nums) if sum(nums,0) == target else result

        while i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j in range(i, n-2):
                pass
