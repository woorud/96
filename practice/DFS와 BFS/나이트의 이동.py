from collections import deque
def _7562():
    def bfs(sx, sy, ex, ey):
        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        q = deque()
        q.append((sx, sy))
        visited[sx][sy] += 1
        while q:
            x, y = q.popleft()
            if x == ex and y == ey:
                print(visited[x][y]-1)
                return
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if  0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


    t = int(input())
    for _ in range(t):
        l = int(input())
        sx, sy = map(int, input().split())
        ex, ey = map(int, input().split())
        visited = [[0]*l for _ in range(l)]
        bfs(sx, sy, ex, ey)

_7562()

