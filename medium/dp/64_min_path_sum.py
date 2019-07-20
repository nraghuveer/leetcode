# https://leetcode.com/problems/minimum-path-sum/

from typing import List

def min_path(grid, dp, point):
    """
        # we have two decisions to make here
        # should we take the left or up
        # we take what-ever gives us the minimum
    """
    i, j = point
    if i == j == 0: # we have no where to go from here, so return
        return grid[0][0]

    # we have this already in dp, return karo!
    if dp[i][j] != -1:
        return dp[i][j]

    grid_val = grid[i][j]

    if i == 0: # we are horizontally blocked, but we can move up
        dp[i][j] = grid_val + min_path(grid, dp, (i, j-1))
    elif j == 0: # we are vertically blocked, but we can move left
        dp[i][j] = grid_val + min_path(grid, dp, (i-1, j))
    else:
        dp[i][j] = grid_val + min(min_path(grid, dp, (i, j-1)),
                        min_path(grid, dp, (i-1, j)))

    return dp[i][j]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid) # height
        n = len(grid[0]) # width

        if m == 0 or n == 0:
            return 0

        if m == 1 and n == 1:
            return grid[0][0]

        dp = [[-1 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]

        # start from the last point
        res  = min_path(grid, dp, (m-1, n-1))

        return res

if __name__ == "__main__":
    ios = [
        ([
  [1,3,1],
  [1,5,1],
  [4,2,1]
], 7)
    ]

    solution = Solution()
    for io in ios:
        res = solution.minPathSum(io[0])
        try:
            assert res == io[1]
        except AssertionError:
            print(f'failed for {io[0]} ==> result {res} ==> expected {io[1]}')

    print('done')