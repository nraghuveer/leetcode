class Solution:

    def removeDuplicateLetters(self, s):
        stack = []
        last = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    s = Solution()
    res = s.removeDuplicateLetters("bcabc")
    print(res)
