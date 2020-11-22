from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j):
    q = deque()
    q.append((i, j))
    tmp = []
    tmp.append((i, j))
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if l <= abs(country[x][y] - country[nx][ny]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    tmp.append((nx, ny))
    return tmp


n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for i in range(n)]

change = 0
while True:
    isTrue = False
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                tmp = bfs(i, j)
                if len(tmp) > 1:
                    isTrue = True
                    num = sum([country[x][y] for x, y in tmp]) // len(tmp)
                    for x, y in tmp:
                        country[x][y] = num
    if not isTrue:
        break
    change += 1

print(change)

