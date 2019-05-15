# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2 = 2 * nums[i2]
            u3 = 3 * nums[i3]
            u5 = 5 * nums[i5]
            umin = min(u2,u3,u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1

            nums.append(umin)
            n -= 1

        return nums.pop()

if __name__ == "__main__":
    solution = Solution()
    assert solution.nthUglyNumber(1) == 1
    assert solution.nthUglyNumber(2) == 2
    assert solution.nthUglyNumber(3) == 3
    assert solution.nthUglyNumber(4) == 4
    assert solution.nthUglyNumber(5) == 5
    assert solution.nthUglyNumber(6) == 6
    assert solution.nthUglyNumber(7) == 8
    assert solution.nthUglyNumber(8) == 9
    assert solution.nthUglyNumber(9) == 10
    assert solution.nthUglyNumber(10) == 12
    print('done')