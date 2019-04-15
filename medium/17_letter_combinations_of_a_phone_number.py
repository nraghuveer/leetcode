mappings = {
    2 : 'abc',
    3 : 'def',
    4 : "ghi",
    5 : 'jkl',
    6 : 'mno',
    7 : 'pqrs',
    8 : 'tuv',
    9 : 'wxyz'
}

class Solution:
    def letterCombinations(self, digits: str):
        digits = [int(i) for i in digits]
        result = []
        for d in digits:
            if not result:
                result = list(mappings[d])
                continue

            new_result = []
            for r in result:
                for m in mappings[d]:
                    new_result.append(r+m)

            result = new_result

        return result

# not mine, but beautiful solution.
# class Solution:
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """

#         if not digits: return []

#         phone = {'2': ['a', 'b', 'c'],
#                     '3': ['d', 'e', 'f'],
#                     '4': ['g', 'h', 'i'],
#                     '5': ['j', 'k', 'l'],
#                     '6': ['m', 'n', 'o'],
#                     '7': ['p', 'q', 'r', 's'],
#                     '8': ['t', 'u', 'v'],
#                     '9': ['w', 'x', 'y', 'z']}
#         result = []

#         # backtracking with helper
#         def helper(i, curr):
#             if i>=len(digits): result.append(curr); return
#             for char in phone[digits[i]]:
#                 helper(i+1, curr+char)

#         helper(0, '')
#         return result

if __name__ == "__main__":
    print(Solution().letterCombinations("234"))
