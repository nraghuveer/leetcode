from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # given time series, these are plots on time starting from 1
        # each attach stays for this duration
        count = 0
        if not timeSeries:
            return count

        count = duration
        prev = timeSeries[0]
        for current in timeSeries[1:]:
            # first update the count
            count += duration
            if (current - prev) < duration:
                count -= duration - (current - prev)
            prev = current

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.findPoisonedDuration([1], 3) == 3
    assert s.findPoisonedDuration([1, 4], 2) == 4
    assert s.findPoisonedDuration([1, 2], 2) == 3
    assert s.findPoisonedDuration([0, 1, 2], 2) == 4
