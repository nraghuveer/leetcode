# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        l = len(nums)
        if l == 2 and nums[0] > nums[1]:
            return l

        prev = nums[0]
        result = 0
        for i in range(1,l):

            local_result = 1
            i_val = nums[i]

            for j in range(i, l):
                if i_val >= nums[j]:
                    local_result += 1

            result = max(result, local_result)

        return result
