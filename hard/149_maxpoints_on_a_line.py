# https://leetcode.com/problems/max-points-on-a-line/

# using slope ?
# if two points have same slope => colinear
# calculate slope for n points with n - 1 points => O(pow(n,2)) => not good

from collections import defaultdict
from typing import List

def gcd(x,y):
    while y:
        x, y = y, x % y

    return x

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """Get max points from given points that are on given lines"""

        if not points:
            return 0

        slope_map = defaultdict(int)
        l = len(points)
        max_count = 0

        for i in range(l):
            curmax = overlap = vertical = 0
            for j in range(i+1, l):
                # if same point, track this to update count
                if points[i] == points[j]:
                    overlap += 1

                # to avoid ZeroDivisionError
                elif points[i][0] == points[j][0]:
                    vertical += 1

                else:
                    x = (points[j][1] - points[i][1])
                    y = (points[j][0] - points[i][0])
                    g = gcd(x,y)
                    x = x/g
                    y = y/g

                    slope_map[(x,y)] += 1
                    curmax = max(curmax, slope_map[(x,y)])

                # incase, zerodivisionerror cases are more => consider vertical
                curmax = max(curmax, vertical)

            # clear the dict, important
            # as the these slope are related with the points[i]
            slope_map.clear()

            # update the global count.
            max_count = max(max_count, curmax + overlap + 1)

        return max_count

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxPoints([[1,1],[2,2],[3,3]]) == 3
    print('done')