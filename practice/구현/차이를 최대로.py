from itertools import permutations
def _10819():
    n = int(input())
    num_list = list(map(int, input().split()))
    m = 0
    for i in permutations(num_list, n):
        i = list(i)
        tmp = 0
        for j in range(n-1):
            tmp += abs(i[j] - i[j+1])
        m = max(m, tmp)
    print(m)

_10819()