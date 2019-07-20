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


# class Solution:
#     def canPartition(self, nums) -> bool:
#         if not nums:
#             return False

#         total_sum = sum(nums)
#         if total_sum % 2 != 0:
#             return False

#         N = len(nums)
#         return self.can_partition(nums, N, 0, 0, total_sum)

#     def can_partition(self, nums, N, cur_sum, index, total):
#         if cur_sum == total/2:
#             return True

#         if index >= N or cur_sum > total/2:
#             return False

#         consider = self.can_partition(nums, N, cur_sum, index + 1, total)
#         dont_consider = self.can_partition(nums, N, cur_sum + nums[index], index + 1, total)

#         return consider or dont_consider


class Solution:
    def canPartition(self, nums) -> bool:
        if not nums:
            return False

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        N = len(nums)
        pass

if __name__ == "__main__":
    print('dine')