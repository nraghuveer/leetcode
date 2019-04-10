# https://www.leetcode.com/problems/3sum

# dont check in the result for the existence
# this took long time for to figure out
# else it would throw TLE.

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        result = []
        if not nums or n < 3:
            return result

        nums = sorted(nums) # asc

        # no need of loop for last three elements.
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = n - 1
            if nums[i] + nums[start] > 0:
                continue

            while start < end:
                if nums[start] + nums[end] + nums[i] == 0:
                    r = sorted([nums[end], nums[start], nums[i]])
                    result.append(r)
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    end -= 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1

                elif nums[start] + nums[end] + nums[i] < 0:
                    start += 1
                else:
                    end -= 1

        return result

if __name__ == "__main__":
    solution = Solution()
    input = [-1,0,1]
    #input =[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(solution.threeSum(input))
    # [[6,-2,-4],[4,0,-4],[3,1,-4],[2,2,-4],[2,0,-2]]
    # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]