# https://leetcode.com/problems/unique-paths-ii/

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid) # height
        n = len(grid[0]) # widht

        if m == 0 or n == 0:
            return 0

        # if the start/end is blocked
        if grid[0][0] or grid[-1][-1]:
            return 0

        # init the memo ds
        dp = [[1 for j in range(n)] for i in range(m)]

        # handle the dp values for first row and columns.
        # they cannot be 1 if they have obstacles infront.

        # first row
        for i in range(1,n):
            # we cannot reach the obstackle
            if grid[0][i]:
                dp[0][i] = 0
            else:
                dp[0][i] = 0 if any(grid[0][:i] ) else 1

        # first column
        for i in range(1,m):
            # we cannot reach the obstrackle
            if grid[i][0]:
                dp[i][0] = 0
            else:
                dp[i][0] = 0 if any([g[0] for g in grid[:i]]) else 1

        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]:
                    dp[i][j] = 0
                else:
                    right = 0 if grid[i-1][j] else dp[i-1][j]
                    down = 0 if grid[i][j-1] else dp[i][j-1]
                    dp[i][j] = right + down

        return dp[-1][-1]

if __name__ == "__main__":
    solution = Solution()

    ios = [
        ([[0,0],[1,1],[0,0]], 0),
        ([[1]], 0),
        ([[0]], 1),

    ]

    for io in ios:
        try:
            res = solution.uniquePathsWithObstacles(io[0])
            assert res == io[1]
        except AssertionError:
            print(f'Failed for {io}, result is {res} ==> expected is {io[1]}')

