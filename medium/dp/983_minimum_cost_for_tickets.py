# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List
INF = float('inf')

########### Top-Down Approach ###############

def min_cost(days, costs, cur_index, N, dp):
    if not days or cur_index >= N:
        return 0

    # we already have the solution, return karo!
    if dp[cur_index] != INF:
        return dp[cur_index]

    # lets check by buying at all costs at this current day
    # buy one-day pass
    one = min_cost(days, costs, cur_index+1, N, dp) + costs[0]
    # buy 7-day pass
    seven_index = cur_index
    for i in range(cur_index, N):
        if days[i] > days[cur_index] + 6:
            break
        seven_index += 1
    seven = min_cost(days, costs, seven_index, N, dp) + costs[1]
    # buy 30-day pass
    thirty_index = cur_index
    for i in range(cur_index, N):
        if days[i] > days[cur_index] + 29:
            break
        thirty_index += 1
    thirty = min_cost(days, costs, thirty_index, N, dp) + costs[2]

    res = min(one, seven, thirty)
    dp[cur_index] = res
    return res

class TopDownSolution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if not days or not costs:
            return 0

        N = len(days)
        dp = [INF] * (N+1)
        return min_cost(days, costs, 0, N, dp)

########### Bottom-Up Approach ###############

# using two arrays for length 366 each...
class BottomUpSolution:
    def mincostTickets(self, days: List[int], costs: List[int]):
        # Lets do this in bottom up approach
        # what is the min cost in which one can travel on a given day
        N = len(days)
        dp = [INF] * (366) # enough ? i think yes ...
        dp[0] = 0
        is_travel_day = [False] * (366)
        for day in days:
            is_travel_day[day] = True

        for i in range(1, 366):
            if not is_travel_day[i]:
                dp[i] = dp[i-1]
                continue

            one = dp[i-1] + costs[0] # can i buy you a ticket today ;)
            # lets think for seven day pass on i
            # a pass which is bought 6 dass past from this day can be used on this day
            seven = dp[i-7] + costs[1] if i - 7 >= 0 else costs[1]
            # think about thirty days, almost done!!
            thirty = dp[i-30] + costs[2] if i - 30 >= 0 else costs[2]

            res = min(one, seven, thirty, dp[i])
            dp[i] = res

        return dp[-1]


##############################################

if __name__ == "__main__":
    Solution = BottomUpSolution
    # Solution = TopDownSolution
    solution = Solution()
    assert solution.mincostTickets([1,4,6,7,8,20], [2,7,15]) == 11
    assert solution.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]) == 17
    print('done')
