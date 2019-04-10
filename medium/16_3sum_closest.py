# https://leetcode.com/problems/3sum-closest/
import sys

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        diff = sys.maxsize
        result = 0
        # sort in ascending order
        nums = sorted(nums)
        n = len(nums)

        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = n - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]
                ldiff = abs(target - total)
                if ldiff == 0:
                    result = total
                    return result

                if ldiff < diff:
                    diff = ldiff
                    result = total

                # ldiff = target - total
                # we want to minimize ldiff, the value of total should increase
                # so move start forward, since ascending hence we get more value
                # to total.
                if target > total:
                    # maxmize total
                    start += 1
                else:
                    end -= 1

        return result

if __name__ == "__main__":
    solution = Solution()
    assert solution.threeSumClosest([0,2,1,-3],1) == 0
    print('done')


