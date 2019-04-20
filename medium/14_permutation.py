# https://leetcode.com/problems/permutations/

from typing import List

def permute(nums, count, result, result_list, level):
    if level == len(count):
        result_list.append(result[:])
        return

    for i in range(len(count)):
        if count[i] == 0:
            continue

        count[i] -= 1
        result[level] = nums[i]
        permute(nums, count, result, result_list, level+1)
        count[i] += 1

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        count = [1] * len(nums)
        result = [None] * len(nums)
        result_list = []
        permute(nums, count, result, result_list, 0)
        return result_list

if __name__ == "__main__":
    r = Solution().permute([0,1])
    print(r)