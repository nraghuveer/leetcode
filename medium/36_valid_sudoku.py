# https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict

def is_valid(row_start, col_start, board, rows, cols):
    """valid function for 3*3 subboard"""
    items = []
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            val = board[i][j]
            if val == '.':
                continue
            if val in items:
                return False
            else:
                items.append(val)
                if val in rows[i]:
                    return False
                else:
                    rows[i].append(val)
                if val in cols[j]:
                    return False
                else:
                    cols[j].append(val)
    return True

class Solution:
    def isValidSudoku(self, board):

        #  Three rules
        # 1 Each row must contain the digits 1-9 without repetition.
        # 2 Each column must contain the digits 1-9 without repetition.
        # 3 Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        rows = defaultdict(list)
        cols = defaultdict(list)
        for i in range(0,8,3):
            for j in range(0,8,3):
                if not is_valid(i, j, board, rows, cols):
                    return False
        return True


if __name__ == "__main__":

    input_true = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
            ]
    input_false = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
                ]

    solution = Solution()
    assert solution.isValidSudoku(input_true) == True
    assert solution.isValidSudoku(input_false) == False
    print('done')

