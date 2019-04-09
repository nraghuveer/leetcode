# https://leetcode.com/problems/zigzag-conversion/

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        going_down = False
        cur_row = 0
        rows = ['']*numRows
        for char in s:
            rows[cur_row] += char
            if cur_row == 0 or cur_row == numRows -1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        return ''.join(rows)

if __name__ == "__main__":
    assert Solution().convert("PAYPALISHIRING",3) == "PAHNAPLSIIGYIR"