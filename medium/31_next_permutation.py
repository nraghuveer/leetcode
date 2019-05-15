# https://leetcode.com/problems/next-permutation/

# this algorithm is given by narayana pandit, indian
# this uses constant space.

# great explanation
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find largest index such that it is last element in array
        # consecutive decreasing values.
        inversion_point = len(nums) - 1
        while inversion_point > 0 and nums[inversion_point-1] >= nums[inversion_point]:
            inversion_point -= 1

        # if inversion point = 0, then all the values of list are in
        # non-increasing order. in that case this is the last permuation
        if inversion_point <= 0:
            self.reverse(nums, 0, len(nums)-1)
            return

        # the pivot is necessarily less than some element in the suffix
        # because we wouldnt get inversion point in first place if it wasnt

        pivot = inversion_point - 1

        j = len(nums) - 1
        while(nums[j] <= nums[pivot]):
            j -= 1

        temp = nums[j]
        nums[j] = nums[pivot]
        nums[pivot] = temp

        # since the suffix is already sorted in decreasing order
        # and swap is done at right place
        # the suffix still remains at decreasing order
        # now reverse the suffix
        self.reverse(nums, inversion_point, len(nums)-1)


    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

            start += 1
            end -= 1

if __name__ == "__main__":
    nums = [1,2,3]
    Solution().nextPermutation(nums)
    print(nums)