# https://leetcode.com/problems/4sum/

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        if n == 0 or n < 4:
            return result

        if n == 4:
            return [sorted(nums)] if sum(nums,0) == target else result

        nums = sorted(nums) # ascending order
        result = []

        for i in range(n-3):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,n-2):
                start = j + 1
                end = n - 1

                while start < end:
                    total = nums[i] + nums[j] + nums[start] + nums[end]
                    if total == target:
                        r = sorted([nums[i], nums[j], nums[start], nums[end]])
                        if r not in result:
                            result.append(r)
                        start += 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                        end -= 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                    elif total < target: # we need greater values, move forward
                        start += 1
                    else: # we need lesser values, move backward
                        end -= 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([-1,0,-5,-2,-2,-4,0,1,-2],-9))

