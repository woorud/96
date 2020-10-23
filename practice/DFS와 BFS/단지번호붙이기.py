n = int(input())
m = [list(map(int, input())) for i in range(n)]

def bfs(m, y, x):
    cnt = 1

    q = [[y, x]]
    m[y][x] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        y, x = q.pop(0)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if m[ny][nx] == 1:
                    cnt += 1
                    m[ny][nx] = 0
                    q.append([ny, nx])
    return cnt

res = []
for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            res.append(bfs(m, i, j))

print(len(res))
for cnt in sorted(res):
    print(cnt)