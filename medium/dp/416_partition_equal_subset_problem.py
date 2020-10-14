# https://leetcode.com/problems/partition-equal-subset-sum/

# given a array of positive only integers
# check if the array can be partitioned into two such that the sum of
# the elements for each subarray should be same

# key points
# 1. The sum of elements of each subarray's can be equal only if the subarray
#       sum is total elements sum / 2.
#    This means the total sum must be even
# 2. Every element of array should be part of either of the subarrays
# 3. so this boils to do the 0/1 knapsack with capacity = sum/2
# 4. Each element should be part of a subset with sum = totalsum/2 then true, else false

from typing import List

def can_partition(nums, N, index, cur_total, target_total):
    if cur_total == target_total:
        return True

    if index >= N or cur_total > target_total:
        return False

    if can_partition(nums, N, index+1, cur_total+nums[index], target_total):
        return True

    next_index = index + 1
    while next_index < N and nums[next_index] == nums[index]:
        next_index += 1

    # dont consider...
    return can_partition(nums, N, next_index, cur_total, target_total)

# def can_partition(nums, N, index, cur_total, target_total):
#     dp = [[False for j in range(target_total+1)] for i in range(N+1)]
#     for i in range(1,N+1):
#         for j in range(1, target_total+1):
#             cur_val = nums[i-1]
#             if j < cur_val:
#                 dp[i][j] = dp[i-1][j]
#             elif j == cur_val:
#                 dp[i][j] = True
#             else:
#                 dp[i][j] = dp[i-1][j] or dp[i-1][j - cur_val]
#     return dp[-1][-1]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        N = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False

        return can_partition(nums, N, index=0, cur_total=0, target_total=total//2)

if __name__ == "__main__":
    solution = Solution()
    assert solution.canPartition([1,5,11,5]) == True
    print('done')