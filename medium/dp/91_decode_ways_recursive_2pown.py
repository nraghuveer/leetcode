# https://leetcode.com/problems/decode-ways/

# note: this solution gives TLE
# O(2^n) - terrible timing !!
# checkout dynamic programming solution for valid solution.

# Time complexity - O(2^n)
# space complexity - O(n)

def decode(s):
    """
    recursive function to decode the string
    """
    if not s:
        return 1

    if s[0] == '0':
        return 0

    # at this point we know we have a valid string
    # check with the second character

    result = 0
    # its better to try and fail, than indexing ;)
    try:
        if int(s[0]+s[1]) < 27:
            result += decode(s[2:])
    except IndexError: # ignore only index errors
        pass
    finally:
        result += decode(s[1:])

    return result

class Solution:
    def numDecodings(self, s: str) -> int:
        return decode(s)

if __name__ == "__main__":
    solution = Solution()
    assert solution.numDecodings('12') == 2
    assert solution.numDecodings('226') == 3
    assert solution.numDecodings('10') == 1
    assert solution.numDecodings('27') == 1
    assert solution.numDecodings('0') == 0
    assert solution.numDecodings('00') == 0
    assert solution.numDecodings('100') == 0
    assert solution.numDecodings('101') == 1
    assert solution.numDecodings('01') == 0
    assert solution.numDecodings('1') == 1
    assert solution.numDecodings('2263') == 3
    print('done')