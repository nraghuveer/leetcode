from typing import List
from math import log


def decimal_to_binary(number, width):
    bnum = to_binary(number)
    return f"{'0'*(width-len(bnum))}{bnum}"

def to_binary(number):
    if number < 2:
        return str(number)
    quotient, remainder = divmod(number, 2)
    result = to_binary(quotient)
    return f"{result}{remainder}"

def binary_to_decimal(binary):
    N = len(binary)
    if N == 1:
        return int(binary)

    i = int(binary[0])
    value = pow(2, N-1) if i == 1 else 0
    return value +  binary_to_decimal(binary[1:])


class Solution:
    def insert_trie(self, trie, binary):
        node = trie
        for b in binary:
            if b not in node:
                node[b] = {}
            node = node[b]

    def complement(self, b):
        return "1" if b=="0" else "0"

    def findMaximumXOR(self, nums: List[int]) -> int:
        maxnum = max(nums)
        width = int(log(maxnum, 2)) + 1 if maxnum > 0 else 1
        bnums = [decimal_to_binary(num, width) for num in nums]
        bresults = []
        trie = {}
        for bnum in bnums:
            self.insert_trie(trie, bnum)
        # search for max for each element
        # calculate the what would be the possible max XOR for each element
        for bnum in bnums:
            root = trie
            bresult = ""
            for b in bnum:
                complement = "1" if b == "0" else "0"
                next_key = complement if complement in root else b
                bresult += "1" if next_key == complement else "0"
                root = root[next_key]
            bresults.append(bresult)
        return max([binary_to_decimal(bnum) for bnum in bresults])


if __name__ == "__main__":
    res = Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
    print(res)
    res = Solution().findMaximumXOR([3,29,15,7,22])
    print(res)
    res = Solution().findMaximumXOR([0,0,5])
    print(res)
    res = Solution().findMaximumXOR([1,1,5])
    print(res)
    res = Solution().findMaximumXOR([1,1,1])
    print(res)
    res = Solution().findMaximumXOR([8,10,2])
    print(res)
    res = Solution().findMaximumXOR([0])
    print(res)