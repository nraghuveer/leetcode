# https://leetcode.com/problems/smallest-integer-divisible-by-k/


# 1 <= K <= 10^5

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:

        if K % 10 not in [1,3,7,9]: return -1;

        mod, mods = 0, set()
        for length in range(1, K+1): # since we can have k remainders ( inc zero)
            mod = (10 * mod + 1) % K
            if mod == 0: return length;

            if mod in mods:
                return -1

            mods.add(mod)
        return -1

if __name__ == "__main__":
    solution = Solution()
    assert solution.smallestRepunitDivByK(19927) == 111