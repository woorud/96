from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(visited, i, j):
    cnt = 0
    q = deque()
    q.append((i, j))
    cnt += 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if farm[nx][ny] == 1 and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return cnt

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    farm = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    res = 0
    for l in range(n):
        for s in range(m):
            if farm[l][s] == 1 and visited[l][s] == False:
                res += bfs(visited, l, s)
    print(res)