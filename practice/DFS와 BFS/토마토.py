from collections import deque


n, m = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(m)]
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            q.append((i, j))

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    q.append((nx, ny))


bfs()

tf = False
res = -2
for i in tomato:
    for j in i:
        if j == 0:
            tf = True
        res = max(res, j)
if tf:
    print(-1)
elif res == -1:
    print(0)
else:
    print(res-1)