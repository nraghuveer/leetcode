from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # first and last house are connected i.e circle
        inc = (0, nums[0])
        ninc = (0, 0)
        # maxh = max(not rob prev house + val, rob prev house)
        for i in range(1, len(nums) - 1):
            inc = (max(*inc), inc[0] + nums[i])
            ninc = (max(*ninc),
                    ninc[0] + nums[i])
        inc = (max(*inc), max(*inc))
        ninc = (max(*ninc), ninc[0]+nums[-1])
        return max(*(inc + ninc))


if __name__ == "__main__":
    s = Solution()
    assert s.rob([2, 3, 2]) == 3
