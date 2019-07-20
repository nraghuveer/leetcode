# https://leetcode.com/problems/unique-paths/

# this would be more of a backtracking than a dp
# but doing backtracking without dp, gives TLE ( uhhhoo )

# backtracking solution - TLE

# def navigate(cur, m, n):
#     if cur == (m-1, n-1):
#         return 1

#     right = 0
#     if cur[0] < m-1:
#         right = navigate((cur[0]+1, cur[1]), m, n)
#     down = 0
#     if cur[1] < n-1:
#         down = navigate((cur[0], cur[1]+1), m, n)

#     return right + down


# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # the goal here is to move from 0,0 to m,n
#         # where we can move either down (x,y+1) or right (x+1,y)
#         return navigate((0, 0), m, n)


# dp solution

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1:
            return 0

        if m == 1 or n == 1:
            return 1

        # fill the dp
        dp = [[1 for j in range(n)] for i in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1] # return last element

if __name__ == "__main__":
    solution = Solution()
    assert solution.uniquePaths(3, 2) == 3
    assert solution.uniquePaths(7, 3) == 28
    print(solution.uniquePaths(23,12))
    print('done')
