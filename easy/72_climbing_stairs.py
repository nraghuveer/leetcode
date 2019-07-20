# https://leetcode.com/problems/climbing-stairs/

# dp[n] = dp[n-1] + dp[n-2]
# we can get to n in two ways
# one step from n-1 and two step from n-2
# therefore f(n) = f(n-1) + f(n-2)
# we can also take one+one step from n-2, but after taking one step => this part of solution
# would be covered by one step from n-1 solution

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        a,b = 1,2

        for i in range(3,n+1):
            a,b = b, a+b

        return b


if __name__ == "__main__":
    solution = Solution()
    solution.climbStairs(4)