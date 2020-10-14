from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals by start
        # for each interval check the others on right
        #   till start <= other start
        #   and end >= other end
        #   if yes, remove the other
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        i = 0
        removed = set()
        while i < n-1:
            if i in removed:
                i += 1
                continue
            j = i+1
            while j < n:
                start, end = intervals[i]
                ostart, oend = intervals[j]
                if ostart > end:
                    break
                if start <= ostart and end >= oend:
                    removed.add(j)
                j += 1
            i += 1
        return n - len(removed)


if __name__ == "__main__":
    s = Solution()
    assert s.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]) == 2
    assert s.removeCoveredIntervals([[1, 4], [2, 3]]) == 1
    assert s.removeCoveredIntervals([[0, 10], [5, 12]]) == 2
    assert s.removeCoveredIntervals([[3, 10], [4, 10], [5, 11]]) == 2
    assert s.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]) == 1
    assert s.removeCoveredIntervals([[34335, 39239], [15875, 91969], [
                                    29673, 66453], [53548, 69161], [40618, 93111]]) == 2
    print("done!")
