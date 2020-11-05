from math import inf

def weight(R, C):
    global N, A, B
    return A * abs(R - C) + B * (N - R * C)

for test_case in range(int(input())):
    N, A, B = [int(i) for i in input().split()]
    res = inf
    for i in range(N):
        for j in range(N):
            if i * j > N:
                break
            v = weight(i, j)
            if v < res:
                res = v

    print("#%d %d" % (test_case + 1, res))
