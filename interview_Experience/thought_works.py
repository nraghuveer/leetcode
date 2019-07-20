
def get_binary_values(number):
    """
    Returns the binary value for the given number
    """
    if not number:
        return [0]

    result = ''
    while number:
        result += str(number % 2)
        number = number // 2
    return list(map(int, list(reversed(result))))

def get_count(number):
    """
    """
    values = get_binary_values(number)
    N = len(values)
    if N == 1:
        return (0,1) if values[0] == 1 else (1,0)

    odd_zeros = [0]
    odd_ones = [0]

    def update_result(counts):
        if counts[0] != 0 and counts[0] % 2 != 0:
            odd_zeros[0] += 1
        if counts[1] != 0 and counts[1] % 2 != 0:
            odd_ones[0] += 1


    dp = [[(None, None) for j in range(N+1)] for i in range(N+1)]
    for i in range(1,N+1):
        val = (0,1) if values[i-1] == 1 else (1,0)
        dp[0][i] = val
        dp[i][0] = val
        update_result(dp[i][0])

    for start in range(1,N+1):
        for end in range(1,N+1):
            if start >= end:
                dp[start][end] = dp[start][end-1]
            else:
                prev = dp[start][end-1]
                dp[start][end] = (prev[0], prev[1]+1) if values[end-1] == 1 else (prev[0]+1, prev[1])
                update_result(dp[start][end])

    return (odd_zeros[0], odd_ones[0])

if __name__ == "__main__":
    for _ in range(int(input())):
        result = get_count(int(input().strip()))
        print(f'{result[0]} {result[1]}')
