import heapq
from fractions import Fraction

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        # first sort in ascending order of the ratio  ( w / q)
        ratios = sorted([(Fraction(w, q), w, q) for w, q in zip(wage, quality)])

        ans = float('inf')
        sumq = 0
        pool = []

        for ratio, w, q in ratios:
            # heap insert into the array with negative value
            # so the min heap turns into max heap bcz python heapq is min heap
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                # remove the highest from the pool, because we just added the least one in above statement
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                # pay every one to according to the ratio
                ans = min(ans, ratio * sumq)

        return float(ans)

if __name__ == "__main__":
    solution = Solution()
    assert solution.mincostToHireWorkers([3,1,10,10,1], wage = [4,8,2,2,7], K = 3) == 30.6667

