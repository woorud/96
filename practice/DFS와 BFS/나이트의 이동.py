from collections import deque
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(a, b, c, d):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        if x == c and y == d:
            print(visited[c][y] - 1)
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1




n = int(input())

for i in range(n):
    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    visited= [[0]*l for _ in range(l)]
    bfs(a, b, c, d)
