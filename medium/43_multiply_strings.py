# https://leetcode.com/problems/multiply-strings/

def rmul(num1, num2):
    n2 = int(num2)

    d = []
    for i, n in enumerate(num1[::-1]):
        d.append(str(int(n)*n2*pow(10,i)))

    return (sum([int(i) for i in d]))

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d = []
        for i, n in enumerate(num2[::-1]):
            d.append(pow(10,i) * rmul(num1, n))

        return str(sum([int(i) for i in d]))

if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply('123','456'))