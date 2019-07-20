
def isPrime(n) :
    # Corner cases
    if (n <= 1) :
        return 0
    if (n <= 3) :
        return 1

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return 0

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return 0
        i = i + 6

    return 1

def run_testcase():
    shape = input()
    shape = [int(size) for size in shape.split(' ')]
    m = shape[0]
    n = shape[1]
    data = []
    for i in range(0, m):
        data.append([isPrime(int(d)) for d in input().split(' ')])

    prime_count = [2]
    comp_count = [-2]

    for i in range(0,m):
        for j in range(0,n):
            explore(data, prime_count, (0,0))
            explore(data, comp_count, (0,0))

def explore(data, count, p):
    """ p-> point . return counts"""
    if not p[0] < m or not p[1] < n:
        return

    if data[p[0]][p[1]] not in (0,1): # already marked
        if count[0] > 0:
            count[0] += 1
        else:
            count[0] -= 1
        return

    # mark and continue
    if count[0] > 0 and data[p[0]][p[1]] == 1:
        data[p[0]][p[1]] = count[0]

    elif count[0] < 0 and data[p[0]][p[1]] == 0:
        data[p[0]][p[1]] = count[0]

    explore(data, count (p[0]+1, p[1]))
    explore(data, count (p[0]-1, p[1]))
    explore(data, count (p[0], p[1]+1))
    explore(data, count (p[0], p[1]-1))
