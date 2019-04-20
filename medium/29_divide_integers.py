class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        temp = 0
        quotient = 0
        for i in range(31,-1,-1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                quotient |= 1 << i # set the ith set for quotient

        if quotient >= ( 1 << 31 ):
            return sign * ( 1 << 31 ) - ( 1 if sign > 0 else 0)

        return sign * quotient

if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(-2147483648,-1))