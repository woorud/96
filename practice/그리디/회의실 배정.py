def _1931():
    n = int(input())
    t = []
    for _ in range(n):
        s, e = map(int, input().split())
        t.append([s, e])

    t = sorted(t, key=lambda x:(x[1],x[0]))

    cnt = 0
    end = 0
    for i in range(len(t)):
        if end <= t[i][0]:
            end = t[i][1]
            cnt += 1
    print(cnt)

_1931()