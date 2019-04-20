# all permuations



def permuate(count, level, result, result_list):
    """ get all permutations """
    if level == len(result):
        result_list.append(''.join([str(i) for i in result]))
        return

    for i in range(0, len(result)):
        if count[i] == 0:
            continue

        result[level] = i+1
        count[i] -= 1
        permuate(count, level+1, result, result_list)
        count[i] += 1

class Solution:
    def getPermutation(self, n: int) -> str:
        result = [None] * n
        count = [1] * n
        result_list = []
        permuate(count, 0, result, result_list)
        return result_list

if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(3))