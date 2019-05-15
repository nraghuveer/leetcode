# https://leetcode.com/problems/perfect-squares/

from math import sqrt, floor

class Solution:
    def isPerfect(self, value):
        """ Checks if the given value is perfect square number """
        return (sqrt(value) - float(sqrt(value))) == 0

    def getPrev(self, value):
        """ returns perfect square that is immediate less than the given value """
        prev = int(sqrt(value))
        return prev ** 2

    def numSquares(self, n: int):
        count = 0
        while n:
            ps = self.getPrev(n)
            n = n - ps
            count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    assert solution.numSquares(12) == 3
