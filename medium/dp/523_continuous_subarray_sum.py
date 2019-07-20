# https://leetcode.com/problems/continuous-subarray-sum/
# TODO

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = {}
        running_sum = 0
        for i in range(l):
            v = nums[i]
            running_sum = (running_sum + v) % k
            if running_sum in m:
                return True
                m[running_sum] = i
        return False

if __name__ == "__main__":
    solution = Solution()
    assert solution.checkSubarraySum([23, 2, 4, 6, 7], 6) == True
    assert solution.checkSubarraySum([23, 2, 3, 4, 7], 6) == False
    assert solution.checkSubarraySum([23,2,6,4,7], 0) == False
    print('done')
