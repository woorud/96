from collections import deque
def _2178():
    def bfs(sx, sy):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()
        q.append((sx, sy))
        visited[sx][sy] += 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and road[nx][ny] == "1":
                    q.append((nx, ny))
                    visited[nx][ny] += visited[x][y]+1



    n, m = map(int, input().split())
    road = [list(input()) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    bfs(0, 0)
    print(visited[-1][-1])

_2178()