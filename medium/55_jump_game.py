# https://leetcode.com/problems/jump-game/

# if zero, we cannot make any jumps from that point

from typing import List

class Status:
    UNKNOWN = 0
    GOOD = 1
    BAD = 2

# there are 4 solutions for this
# 1. Recursion
# 2. DP - top down
# 3. DP - bottom up
# 4. Greedy

############## Recursive / Backtracking Solution #################

# def recursive_solution(nums):
#     """Recursive solution or backtracking solution"""
#     return can_jump_from_position(0, nums)

# def can_jump_from_position(position, jumps):
#     """ Can we jump to end from this position """
#     if position == len(jumps) - 1:
#         return True

#     max_reach = min(position + jumps[position], len(jumps)-1)
#     # iterate from current point to the max reach point
#     # for each point check we can jump from that point
#     # if yes, return TRue else check for other points
#     # if not points is True, return False
#     for j in range(position + 1, max_reach+1):
#         if can_jump_from_position(j, jumps):
#             return True
#     return False

############ DP - Top Down Approach ###########################

# def top_down_solution(jumps):
#     """ DP - Top - Down Solution """
#     dp = [Status.UNKNOWN] * len(jumps)
#     # assume last point is reachable
#     dp[-1] = Status.GOOD
#     return can_jump_from_position(0, dp, jumps)

# def can_jump_from_position(position, dp, jumps):
#     if dp[position] != Status.UNKNOWN:
#         return True if dp[position] == Status.GOOD else False

#     max_reach = min(position + jumps[position], len(jumps)-1)
#     # iterate from current point to the max reach point
#     # for each point check we can jump from that point
#     # if yes, return TRue else check for other points
#     # if not points is True, return False
#     for j in range(position + 1, max_reach+1):
#         if can_jump_from_position(j, dp, jumps):
#             dp[position] = Status.GOOD
#             return True
#     dp[position] = Status.BAD
#     return False


#################### DP - Bottom Up Apprach ###############

# def bottom_up_solution(jumps):
#     """ DP - bottom up solutions """
#     dp = [Status.UNKNOWN] * len(jumps)
#     dp[-1] = Status.GOOD
#     for i in range(len(jumps)-2,-1,-1):
#         max_reach = min(i + jumps[i], len(jumps)-1)
#         # from this point, can we reach any of the good points ?
#         for j in range(i+1, max_reach+1):
#             if dp[j] == Status.GOOD:
#                 dp[i] = dp[j]
#                 break

#     return dp[0] == Status.GOOD

######################## Greedy Approach #####################

######################## Efficient and Clean Solution ########
def greedy_solution(nums):
    """ Greedy SOlution """
    last_pos = len(nums) -1
    for i in range(len(nums)-2, -1,-1):
        if i + nums[i] >= last_pos:
            last_pos = i

    return last_pos == 0

####################### More more efficient and not so clean solution ##
def greedy_solution2(jumps):
    k = 1
    for i in range(len(jumps)-2,-1,-1):
        k = k + 1 if jumps[i] < k else 1
    return k == 1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return greedy_solution(nums)

if __name__ == "__main__":
    solution = Solution()
    assert solution.canJump([0]) == True
    assert solution.canJump([0,1]) == False
    assert solution.canJump([1]) == True
    assert solution.canJump([1,0]) == True
    assert solution.canJump([1,2]) == True
    assert solution.canJump([1,2,3]) == True
    assert solution.canJump([2,3,1,1,4]) == True
    assert solution.canJump([3,2,1,0,4]) == False
    assert solution.canJump([4,2,0,0,1,1,4,4,4,0,4,0]) == True
    print('done')