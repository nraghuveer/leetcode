# https://leetcode.com/problems/decode-ways-ii/

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        l = len(s)
        M = 10**9 + 7
        dp = [0]*(l + 1)

        dp[0] = 1
        if s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1

        for i in range(2, l+1):
            v = s[i-1]
            pv = s[i-2]

            if v == '*':
                res = 9 * dp[i-1]
                # noting to add incase of zero, so ignore that case.
                if pv == '1':
                    res =  (res + 9 * dp[i-2]) % M
                elif pv == '2':
                    res = (res + 6 * dp[i-2]) % M
                elif pv == '*':
                    res = (res + 15 * dp[i-2]) % M

            else:
                # current is [1-9]
                res = dp[i-1] if v != '0' else 0
                if pv == '1' or (pv == '2' and v < '7'):
                    res = (res + dp[i-2]) % M # tricky
                elif pv == '*':
                    res = (res + (2 if v < '7' else 1) * dp[i-2]) % M

            dp[i] = res

        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    assert solution.numDecodings('1') == 1
    assert solution.numDecodings('12') == 2
    assert solution.numDecodings('226') == 3
    assert solution.numDecodings('10') == 1
    assert solution.numDecodings('27') == 1
    assert solution.numDecodings('0') == 0
    assert solution.numDecodings('00') == 0
    assert solution.numDecodings('100') == 0
    assert solution.numDecodings('1000') == 0
    assert solution.numDecodings('101') == 1
    assert solution.numDecodings('01') == 0
    assert solution.numDecodings('1') == 1
    assert solution.numDecodings('2263') == 3
    assert solution.numDecodings('*') == 9
    assert solution.numDecodings('1*') == 18
    assert solution.numDecodings('0*') == 0
    assert solution.numDecodings('**') == 96
    assert solution.numDecodings('*1') == 11
    assert solution.numDecodings('**1**') == 18720
    print('done')