class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        for index, value in enumerate(reversed(s)):
            realvalue = ord(value) - 64
            total += pow(26, index) * realvalue
        return total


if __name__ == "__main__":
    ret = Solution().titleToNumber("ZY")
    ret = Solution().titleToNumber("AAA")
    print(ret)
