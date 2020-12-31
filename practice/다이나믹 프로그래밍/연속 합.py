def _1912():
    n = int(input())
    num_list = list(map(int, input().split()))
    tmp = [0 for i in range(n)]
    m = -1001

    for i in range(n):
        tmp[i] = max(tmp[i-1]+num_list[i], num_list[i])
        m = max(tmp[i], m)

    return m

print(_1912())
