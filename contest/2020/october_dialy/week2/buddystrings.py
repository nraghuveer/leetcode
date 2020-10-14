from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) < len(A)
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]


if __name__ == "__main__":
    s = Solution()
    assert s.buddyStrings("abab", "abab")
    assert s.buddyStrings("ab", "ba") == True
    assert not s.buddyStrings("ab", "ab")
    assert s.buddyStrings("aa", "aa")
    assert s.buddyStrings("aaaaaabc", "aaaaaacb")
    assert not s.buddyStrings("", "aa")
    assert not s.buddyStrings("df", "fh")
    assert not s.buddyStrings("", "")
    assert s.buddyStrings("aaab", "aaab")
    print('done')
