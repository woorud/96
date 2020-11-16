from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited = [[0] * h for _ in range(w)]
    visited[i][j] = 1
    t = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if map[nx][ny] == "L" and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    t = max(t, visited[nx][ny])
    return t-1


w, h = map(int, input().split())
map = [list(input()) for _ in range(w)]

res = []
for i in range(w):
    for j in range(h):
        if map[i][j] == "L":
            res.append(bfs(i, j))

print(max(res))
