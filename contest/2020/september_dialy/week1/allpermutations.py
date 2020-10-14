from pprint import pprint


def generate_permutations(arr, N):
    count = [1] * N
    result = []
    result_stack = [-1] * N
    _generate(arr, N, 0, count, result_stack, result)
    return result


def _generate(arr, N, level, count, result_stack, result):
    if level == N:
        result.append(result_stack[:])
        return

    for i in range(N):
        if count[i] == 0:
            continue

        result_stack[level] = arr[i]
        count[i] -= 1
        _generate(arr, N, level + 1, count, result_stack, result)
        count[i] += 1


if __name__ == "__main__":
    res = generate_permutations([1, 2, 3, 4], 4)
    pprint(res)
