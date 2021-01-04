from collections import deque
def _7576():
    def bfs():
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()
        for i in range(n):
            for j in range(m):
                if tomato[i][j] == 1:
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                    q.append((nx, ny))
                    tomato[nx][ny] += tomato[x][y] + 1

    m, n = map(int, input().split())
    tomato = [list(map(int, input().split())) for _ in range(n)]

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


_7576()
