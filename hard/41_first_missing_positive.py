from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # missing positive integer of a array of size N can range from 1 to N+1
        N = len(nums)
        # remove the values which dont consititute in the final answer
        # that 0 and values > N+1
        # we do that by putting max value N+1 in place of those values
        for i in range(N):
            if nums[i] <= 0 or nums[i] > N:
                nums[i] = N+1

        # mark the index
        for i in range(N):
            num = abs(nums[i])
            # mark that this number is already seen so it cant be the answer
            if num > N:
                continue
            num -= 1
            if nums[num] > 0:
                nums[num] = -1*nums[num]

        for i in range(N):
            if nums[i] >= 0:
                return i+1

        return N+1


if __name__ == "__main__":
    solution = Solution()
    assert solution.firstMissingPositive([3,4,-1,1]) == 2
