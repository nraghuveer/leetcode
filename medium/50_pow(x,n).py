# https://leetcode.com/problems/powx-n/


def pow(x, n):

    # the basic idea is to divide the problem into small pieces that
    # it comes down to pow(x,0), which value is 1
    # if pow(x,n)
    # if n is even i.e. n%2==0, then pow(x,n) = pow(x,n/2)*pow(x,n/2)
    #   becuase X^n * X^m = X^(n+m)
    # if n is odd, then pow(x,n) = x * pow(x,n/2)*pow(x,n/2)
    if n == 0:
        return 1

    temp = pow(x, int(n/2))
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp


class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_pve = n >= 0
        res = pow(x, abs(n))
        return res if is_pve else 1/res


if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2, -2))
