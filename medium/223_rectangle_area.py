# https://leetcode.com/problems/rectangle-area/

from collections import namedtuple

Point = namedtuple('Point', 'x y')

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        l1 = Point(x=A,y=B)
        l2 = Point(x=E,y=F)
        r1 = Point(x=C,y=D)
        r2 = Point(x=G,y=H)

        a1 = abs(l1.x - r1.x) * abs(l1.y - r1.y)
        a2 = abs(l2.x - r2.x) * abs(l2.y - r2.y)

        # intersection rectangle lengths.
        i_x = min(r1.x, r2.x) - max(l1.x, l2.x)
        i_y = min(r1.y, r2.y) - max(l1.y, l2.y)

        if (i_x < 0) | (i_y < 0):
            ai = 0
        else:
            ai = i_x * i_y

        return a1 + a2 - ai

if __name__ == "__main__":
    Solution().computeArea(-2,
-2,
2,
2,
3,
3,
4,
4)