# https://leetcode.com/problems/roman-to-integer/

from collections import OrderedDict

roman = OrderedDict({
    'M' : 1000,
    'CM' : 900,
    'D' : 500,
    'CD' : 400,
    'C' : 100,
    'XC' : 90,
    'L' : 50,
    'XL' : 40,
    'X' : 10,
    'IX' : 9,
    'V' : 5,
    'IV' : 4,
    'I' : 1
})

def from_roman(s: str) -> int:
    if not s:
        return 0

    n = len(s)

    if n == 1:
        return roman[s[0]]

    # special cases
    # IV, IX, XL, XC, CD, CM
    elif s[0:2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
        return roman[s[0:2]] + from_roman(s[2:])

    else:
        return roman[s[0]] + from_roman(s[1:n])

class Solution:
    def romanToInt(self, s: str) -> int:
        return from_roman(s)

if __name__ == "__main__":
    solution = Solution()

    assert solution.romanToInt('III') == 3
    assert solution.romanToInt('IV') == 4
    assert solution.romanToInt('IX') == 9
    assert solution.romanToInt('LVIII') == 58
    assert solution.romanToInt('MCMXCIV') == 1994
    print('done')