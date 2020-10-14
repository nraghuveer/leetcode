from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # remember the original order
        arr = [(index, num) for index, num in enumerate(nums)]
        # now sort with value in ascending order
        arr = sorted(arr, key=lambda x: x[1])
        # so traverse
        # go atmost k
        N = len(arr)
        j = 1
        i = 0
        while j < N:
            # check the difference
            diff = abs(arr[i][1] - arr[j][1])
            distance = abs(arr[i][0] - arr[j][0])
            if diff <= t and distance <= k:
                return True

            if diff > t:
                # change to the next unique value
                i = i + 1
                j = i + 1
            else:
                j += 1
        return False


if __name__ == "__main__":
    res = Solution().containsNearbyAlmostDuplicate([1,2,1,1], 1, 0)
    print(res)
