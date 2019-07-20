# given a number, get the binary format of that number
# and get the number of substrings with odd number of zeros and odd number of ones

def get_binary_values(number):
    """
    Returns the binary value for the given number
    """
    if not number:
        return [0]

    result = []
    while number:
        result.append(number % 2)
        number = number // 2
    return list(reversed(result))

def get_count(number):
    """
    """
    values = get_binary_values(number)
    N = len(values)
    if N == 1:
        return (0,1) if values[0] == 1 else (1,0)

    odd_zeros = 0
    odd_ones = 0

    dp = [(None, None) for j in range(N+1)]
    for start in range(1,N+1):
        val = (0,1) if values[start-1] == 1 else (1,0)
        dp[0] = val
        if val[0] != 0 and val[0] % 2 != 0:
            odd_zeros += 1
        if val[1] != 0 and val[1] % 2 != 0:
            odd_ones += 1

        for end in range(1,N+1):
            if start >= end:
                dp[end] = dp[end-1]
            else:
                prev = dp[end-1]
                cur = (prev[0], prev[1]+1) if values[end-1] == 1 else (prev[0]+1, prev[1])
                dp[end] = cur
                if cur[0] != 0 and cur[0] % 2 != 0:
                    odd_zeros += 1
                if cur[1] != 0 and cur[1] % 2 != 0:
                    odd_ones += 1

    return (odd_zeros, odd_ones)

if __name__ == "__main__":
    for _ in range(int(input())):
        result = get_count(int(input().strip()))
        print(f'{result[0]} {result[1]}')
