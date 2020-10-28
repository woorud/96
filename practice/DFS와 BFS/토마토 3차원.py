from collections import deque

m, n, h = map(int, input().split())
floors = []
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
    floors.append(tmp)

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if floors[i][j][k] == 1:
                q.append((i, j, k))


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

while q:
    height, row, col = q.popleft()
    for i in range(6):
        nh = height + dh[i]
        nr = row + dy[i]
        nc = col + dx[i]

        if 0 <= nh < h and 0 <= nr < n and 0 <= nc < m and floors[nh][nr][nc] == 0:
            q.append((nh, nr, nc))
            floors[nh][nr][nc] = floors[height][row][col] + 1

isTrue = False
res = -2

for i in floors:
    for j in i:
        for k in j:
            if k == 0:
                isTrue = True
            res = max(res, k)

if isTrue:
    print(-1)
elif res == -1:
    print(0)
else:
    print(res-1)
















