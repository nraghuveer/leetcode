# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0]*(n+1)

        # do some babysitting :)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        # time for some action !! ( boom boom bang bang )
        for i in range(3,n+1):

            max_val = 0
            for j in range(1, i):

                max_val = max(max_val, j*(i-j))
                dp[i] = max(dp[i], max_val, j*dp[i-j], dp[j]*(i-j))

            print(f'result for {i} : {dp[i]}')

        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    solution.integerBreak(13)