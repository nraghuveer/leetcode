class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # find the first non space character
        index = len(s) - 1
        while index > -1:
            if s[index] != " ":
                break
            index -= 1
        else:
            return 0

        wlen = 0
        while index > -1:
            if s[index] == " ":
                break
            wlen += 1
            index -= 1

        return wlen

if __name__ == "__main__":
    res = Solution().lengthOfLastWord("a ")
    print(res)