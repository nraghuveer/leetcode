from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # remove range if it is inside another range
        # sort the points in ascending order
        if not points:
            return 0
        points = sorted(points, key=lambda x: (x[0], x[-1]))
        start, end = points[0]
        last = end
        index = 1
        count = 1
        while index < len(points):
            cstart, cend = points[index]
            # see if we can increase the range
            # increase the range start of cur is in range of existing
            if start <= cstart <= end and cstart <= last:
                last = min(last, cend)
                end = max(end, cend)
            else:
                start, end, last = cstart, cend, cend
                count += 1
            index += 1
        return count

    def findMinArrowShots2(self, points):
        if not points:
            return 0
        # sort the poitns with end in ascending
        points = sorted(points, key=lambda x: x[1])
        count = 1
        cur = points[0][1]
        for index, (start, end) in enumerate(points[1:]):
            if start <= cur <= end:
                continue
            else:
                cur = end
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.findMinArrowShots2([]) == 0
    assert s.findMinArrowShots2([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert s.findMinArrowShots2([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert s.findMinArrowShots2([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert s.findMinArrowShots2([[1, 2]]) == 1
    assert s.findMinArrowShots2([[2, 3], [2, 3]]) == 1
    assert (
        s.findMinArrowShots2(
            [
                [3, 9],
                [7, 12],
                [3, 8],
                [6, 8],
                [9, 10],
                [2, 9],
                [0, 9],
                [3, 9],
                [0, 6],
                [2, 8],
            ]
        )
        == 2
    )
    print("Done!")


"""
1            6
   2              8
                7           12
                      10              16

             ^         ^
             |         |
=============================================
1      6
  2             8



"""