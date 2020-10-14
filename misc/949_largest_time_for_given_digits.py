from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr) -> str:
        items = permutations(arr, 4)
        items = [(int(f"{i[0]}{i[1]}"), int(f"{i[2]}{i[3]}")) for i in items]
        items = [i for i in items if i[0] < 24 and i[1] < 60]
        sitems = sorted(items, key=lambda k: (k[0], k[1]))
        if not sitems:
            return ""
        ans = sitems[-1]
        return f"{ans[0]}:{ans[1]}"


if __name__ == "__main__":
    ans = Solution().largestTimeFromDigits([1, 2, 3, 4])
    print(ans)

