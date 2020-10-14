class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        c = [[1 if i==j else 0 for i in range(N)] for j in range(N)]
        # get for the length of 2
        k = 2
        i = 0
        while i < N-1:
            j = i + 1
            c[i][j] = 2 if s[i] == s[j] else 1
            i += 1
        # for the length of 3
        i = 0
        while i < N - 2:
            j = i + 2
            c[i][j] = 2 + c[i+1][j-1] if s[i]==s[j] else max(c[i+1][j], c[i][j-1])
            i += 1

        k = 3
        while k < N:
            i = 0
            while i < (N-k):
                j = i + k
                c[i][j] = 2 + c[i+1][j-1] if s[i]==s[j] else max(c[i+1][j], c[i][j-1])
                i += 1
            k += 1
        return c[0][N-1]


if __name__ == "__main__":
    ret = Solution().longestPalindromeSubseq("agbdba")
    print(ret)