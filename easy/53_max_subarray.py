# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the
# contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

from typing import List

def max_sub_arr(nums, dp, i):
    if i == 0:
        dp[i] = nums[0]
        return dp[i]

    p =  max_sub_arr(nums, dp, i-1)
    # return max of current+prev and current
    dp[i] = max(nums[i], nums[i] + p)
    return dp[i]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = len(nums)
        if l == 1:
            return nums[0]

        dp = [-1]*l

        max_sub_arr(nums, dp, l-1)

        return max(dp)

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert solution.maxSubArray([1,-1,-2]) == 1
    print('done')