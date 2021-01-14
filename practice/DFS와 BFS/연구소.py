from collections import deque
import copy
def _14502():
    def area(arr):
        s = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    s += 1
        return s

    def bfs():
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        c_maps = copy.deepcopy(maps)

        q = deque()
        visited = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if c_maps[i][j] == 2:
                    q.append((i, j))
                    visited[i][j] = True

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and c_maps[nx][ny] == 0 and visited[nx][ny] == False:
                    q.append((nx, ny))
                    c_maps[nx][ny] = 2
                    visited[nx][ny] = True
        return area(c_maps)

    res = []
    def wall(cnt):
        if cnt == 3:
            res.append(bfs())
            return
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 0:
                    maps[i][j] = 1
                    wall(cnt+1)
                    maps[i][j] = 0

    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    wall(0)
    print(max(res))

_14502()