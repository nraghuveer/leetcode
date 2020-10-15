from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort with first element and second element descending
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        index = 1
        start, end = intervals[0]
        ans = []
        while index < len(intervals):
            cstart, cend = intervals[index]
            if start <= cstart <= end:
                end = max(end, cend)
            else:
                ans.append([start, end])
                start, end = cstart, cend
            index += 1
        ans.append([start, end])
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [0, 2], [3, 5]]) == [[0, 5]]
    assert s.merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert s.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert s.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [1, 10]
    print("Done!")