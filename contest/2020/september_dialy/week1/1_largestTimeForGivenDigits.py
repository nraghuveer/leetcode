# The hardest part of the problem is generating all the permutation
# for the given digits

from typing import List
# if the digits are in chronological order, first valid time is correct answer!
from allpermutations import generate_permutations


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr = sorted(arr, reverse=True)
        permutations = generate_permutations(arr, len(arr))
        for item in permutations:
            if self.is_vaild_time(item):
                return f"{item[0]}{item[1]}:{item[2]}{item[3]}"
        return ""

    def is_vaild_time(self, item):
        hour = int(f"{item[0]}{item[1]}")
        minute = int(f"{item[2]}{item[3]}")
        return hour < 24 and minute < 59


if __name__ == "__main__":
    res = Solution().largestTimeFromDigits([1, 9, 6, 0])
    print(res)
