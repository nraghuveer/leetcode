# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        max_area = 0
        start = 0
        end = n - 1
        while start < end and end > start:
            max_area = max(max_area, min(height[start],height[end])*(end-start))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_area

if __name__ == "__main__":
    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
