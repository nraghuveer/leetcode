# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = ''
        if s[0] in ['+', '-']:
            sign = s[0]
            s = s[1:]
        result = []
        try:
            for c in s:
                int(c)
                result += c
        except ValueError:
            pass

        if not result:
            return 0

        result = int('{}{}'.format(sign, ''.join(result)))
        if result <= pow(-2,31):
            return pow(-2,31)
        elif result >= pow(2,31):
            return pow(2,31) - 1

        return result

if __name__ == "__main__":
    Solution().myAtoi("words and 4")
