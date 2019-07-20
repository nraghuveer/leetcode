# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.linear_solution(nums)


    def linear_solution(self,array):
        """ Linear solution - O(N) Time and constant space """
        if len(array) < 2: return 0;

        # max point to which we can reach from this point
        # since this is first point, we have to use this
        # max_reach = i + array[i]
        max_reach = 0 + array[0] # storing the longest laddder
        steps = array[0] # stairs
        jumps = 0
        for i in range(1, len(array) - 1):
            max_reach = max(max_reach, i + array[i])
            # go down on the current ladder
            steps -= 1
            if steps == 0: # end of current ladder, make jump
                jumps += 1
                steps = max_reach - i # pick the longest stored ladder, continue from current point

        return jumps + 1