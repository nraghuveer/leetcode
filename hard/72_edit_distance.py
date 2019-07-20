# https://leetcode.com/problems/edit-distance/
# https://www.algoexpert.io/questions/Levenshtein%20Distance

# a function that takes two strings and returns noof edit operations that needed
# to be performed on the first string to obtain second string

# edit operations
# 1. insertion, 2. deletion, 3. substitution

# left -> deletion
# up -> insertion
# diagonal -> replacement

# we only need two rows as dp here.

# Time : O(NM)
# Space : O(min(N,M))

class Solution:
    def minDistance(self, str1, str2):
        N = len(str1)
        M = len(str2)
        if not str1 or not str2:
            return max(N,M)

        # make N small and M big
        if N != M and max(N,M) == N:
            tmp = str2
            str2 = str1
            str1 = tmp
            N = len(str1)
            M = len(str2)

        dp = [[i for i in range(N+1)] for j in range(2)]
        dp[1][0] = 1

        for i in range(1,M+1):
            for j in range(1,N+1):
                if str2[i-1] == str1[j-1]:
                    dp[1][j] = dp[0][j-1] # diagonal
                else:
                    dp[1][j] = 1 + min(
                                        dp[1][j-1], # left
                                        dp[0][j], # up
                                        dp[0][j-1]
                                        )

            dp[0] = dp[1][:]
            dp[1][0] = dp[0][0]+1

        return dp[-1][-1]
