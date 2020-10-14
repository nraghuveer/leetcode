# https://leetcode.com/problems/palindrome-partitioning/

from typing import List

def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def decompose(s, n, start, current_decompositions, valid_decompositions):
    """ recursive function """
    if start == n:
        valid_decompositions.append(current_decompositions[:])
        return

    for i in range(start, n):
        if not is_palindrome(s, start, i):
            continue

        current_decompositions.append(s[start:i+1])
        decompose(s, n, i+1, current_decompositions, valid_decompositions)
        current_decompositions.pop()

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        current_decompositions = []
        valid_decompositions = []
        decompose(s, len(s), 0, current_decompositions, valid_decompositions)
        return valid_decompositions


if __name__ == "__main__":
    solution = Solution()
    solution.partition('aab')
    solution.partition('noon')