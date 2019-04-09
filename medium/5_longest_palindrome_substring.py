# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        T = [[False if i!=j else True for i in range(n)] for j in range(n)]

        i = 0
        start = 0
        max_len = 1
        while i < (n-1):
            if s[i] == s[i+1]:
                T[i][i+1] = True
                start = i
                max_len = 2
            i += 1

        k = 3
        while k <= n:
            i = 0
            while i <= (n - k):
                j = i + k - 1
                if s[i] == s[j] and T[i+1][j-1] == True:
                    T[i][j] = True
                    start = i
                    max_len = k

                i += 1
            k += 1

        print(max_len)
        print(s[start : start+max_len])

if __name__ == "__main__":
    Solution().longestPalindrome("adsfghhgasdf")