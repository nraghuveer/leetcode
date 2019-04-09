# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        cur_len = 1
        max_len = 1

        visited = [-1]*256 # consider ascii charset
        visited[ord(s[0])] = 0

        for i in range(1, len(s)):
            prev_index = visited[ord(s[i])]
            if prev_index == -1 or (i - cur_len) > prev_index:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len

                cur_len = i - prev_index

            visited[ord(s[i])] = i

        return cur_len if cur_len > max_len else max_len


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))
