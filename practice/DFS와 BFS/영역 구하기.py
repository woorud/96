from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = []
def bfs(i, j):
    q = deque()
    q.append((i, j))
    area[i][j] = 1
    w = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0 <= ny < n:
                if area[nx][ny] == 0:
                    area[nx][ny] = 1
                    w += 1
                    q.append((nx, ny))

    res.append(w)



m, n, k = map(int, input().split())
area = [[0]*n for i in range(m)]
for i in range(k):
    a, b, c, d = map(int, input().split())
    for j in range(a, c):
        for k in range(b, d):
            area[k][j] = 1

for i in range(m):
    for j in range(n):
        if area[i][j] == 0:
            bfs(i, j)
print(len(res))
for i in sorted(res):
    print(i, end = ' ')


