# https://leetcode.com/problems/self-crossing/

# incomplete !!! -- too hard

class Solution:
    def isSelfCrossing(self, x):
        l = len(x)
        if l <= 3:
            return False

        for i in range(x):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True



if __name__ == "__main__":
    solution = Solution()
    assert solution.isSelfCrossing([2,1,1,2]) == True
    assert solution.isSelfCrossing([1,2,3,4]) == False
    assert solution.isSelfCrossing([1,2,2,3,4]) == False
    assert solution.isSelfCrossing([1,1,2,1,1]) == True
    assert solution.isSelfCrossing([1,1,2,2,1,1]) == True
    assert solution.isSelfCrossing([2,1,4,4,3,3,2,1,1]) == True
    print('done')