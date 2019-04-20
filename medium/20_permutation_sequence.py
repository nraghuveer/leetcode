# https://leetcode.com/problems/permutation-sequence/
"""The idea is as follow:

For permutations of n, the first (n-1)! permutations start with 1, next (n-1)! ones start with 2, ... and so on. And in each group of (n-1)! permutations, the first (n-2)! permutations start with the smallest remaining number, ...

take n = 3 as an example, the first 2 (that is, (3-1)! ) permutations start with 1,
next 2 start with 2 and last 2 start with 3. For the first 2 permutations (123 and 132),
the 1st one (1!) starts with 2, which is the smallest remaining number (2 and 3).
So we can use a loop to check the region that the sequence number falls in and get the starting digit.
Then we adjust the sequence number and continue.
"""
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ''
        l = list(range(1,n+1))
        k -= 1
        while n > 0:
            n -= 1
            i, k = divmod(k, math.factorial(n))
            result += str(l.pop(i))

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(5, 30))