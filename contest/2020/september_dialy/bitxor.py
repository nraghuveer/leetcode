
def findMaximumXOR(nums):
    answer = 0
    for i in range(5)[::-1]:
        answer <<= 1
        prefixes = {num >> i for num in nums}
        answer += any(answer^1 ^ p in prefixes for p in prefixes)
    return answer


if __name__ == "__main__":
    print(findMaximumXOR([8,10,2]))