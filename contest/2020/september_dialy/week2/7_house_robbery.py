from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # at each house we will have two options
        # Not rob this, rob this
        dp = (0, nums[0])
        for house_number, value in enumerate(nums[1:], 1):
            # if we choose to not rob it, take the value of the what would
            # be if we rob the prev house
            not_robbed_value = max(*dp)
            robbed_value = dp[0] + value
            dp = (not_robbed_value, robbed_value)
        return max(not_robbed_value, robbed_value)


if __name__ == "__main__":
    res = Solution().rob([1,1,1,1,1,1,1])
    print(res)