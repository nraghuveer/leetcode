# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N

        n1 = 0
        n2 = 1

        for i in range(2, N+1):
            n1, n2 = n2, n1 + n2

        return n2

if __name__ == "__main__":
    solution = Solution()
    assert solution.fib(5) == 5
    print('done')