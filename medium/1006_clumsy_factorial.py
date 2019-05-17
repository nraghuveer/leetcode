# https://leetcode.com/problems/clumsy-factorial/

class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 6
        elif N == 4:
            return 7
        else:
            rmd = N%4
            if rmd == 0:
                return N + 1
            elif rmd == 1 or rmd == 2:
                return N + 2
            else:
                return N -1

if __name__ == "__main__":
    solution = Solution()
    for i in range(6,18):
        print(f'{i} ==> {solution.clumsy(i)}')
        print('======================')
    assert solution.clumsy(0) == 1
    assert solution.clumsy(1) == 1
    assert solution.clumsy(4) == 7
    assert solution.clumsy(10) == 12