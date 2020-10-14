# uses buckets

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}
        i = 0
        N = len(nums)
        w = t + 1
        while i < N:
            bucketid = nums[i] // w
            if bucketid in buckets:
                return True
            elif bucketid + 1 in buckets and abs(nums[i] - buckets[bucketid + 1]) < w:
                return True
            elif bucketid - 1 in buckets and abs(nums[i] - buckets[bucketid - 1]) < w:
                return True
            buckets[bucketid] = nums[i]
            # remove the item if it is out of sliding window
            if i >= k:  # to avoid base condition first k elements in array
                del buckets[nums[i - k] // w]
            i += 1
        return False

if __name__ == "__main__":
    res = Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3)
    print(res)