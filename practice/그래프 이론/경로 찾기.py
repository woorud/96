def _11403():
    n = int(input())
    route = [list(map(int, input().split())) for _ in range(n)]

    for k in range(n):
        for a in range(n):
            for b in range(n):
                if route[a][k] == 1 and route[k][b] == 1:
                    route[a][b] = 1
    for i in route:
        for j in i:
            print(j, end = ' ')
        print()

_11403()