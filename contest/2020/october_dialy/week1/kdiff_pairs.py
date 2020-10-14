from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # in the number line, we can move k steps forward and k steps backward
        # we only move forward because, to avoid duplicates
        # we can also move only backward
        # |x - (x+k)| and |x - (x-k)|, both value will be k
        if k == 0:
            return sum([v > 1 for v in Counter(nums).values()])
        elif k < 0:
            return 0  # absolute value cannot be 0
        return len(set(nums) & set([i+k for i in nums]))


if __name__ == "__main__":
    result = Solution().findPairs([1, 2, 3, 4, 5], 1)
    assert result == 4
    assert Solution().findPairs([3, 1, 4, 1, 5], 2) == 2
    assert Solution().findPairs([1, 3, 1, 5, 4], 0) == 1
    assert Solution().findPairs([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3) == 2
    assert Solution().findPairs([-1, -2, -3], 1) == 2
