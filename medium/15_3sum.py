# https://www.leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums):
        nums = sorted(nums, reverse=True) # desc
        n = len(nums)
        result = []
        for i in range(n):
            # X + a + b = 0
            # X is nums[i], find a and b
            X = nums[i]
            ai = i + 1
            bi = n - 1
            while ai < bi:
                sum = nums[ai] + nums[bi]
                if sum == -X:
                    # put in asc order.
                    r = [nums[bi], nums[ai], nums[i]]
                    if r not in result:
                        result.append(r)
                    break
                elif sum > -X:
                    ai += 1
                elif sum < -X:
                    bi -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
    # [[6,-2,-4],[4,0,-4],[3,1,-4],[2,2,-4],[2,0,-2]]
    # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]