from collections import deque
def _7569():
    def bfs():
        dz = [0, 0, 0, 0, -1, 1]
        dx = [-1, 1, 0, 0, 0, 0]
        dy = [0, 0, -1, 1, 0, 0]

        q = deque()
        for k in range(h):
            for i in range(n):
                for j in range(m):
                    if tomato[k][i][j] == 1:
                        q.append((k, i, j))

        while q:
            z, x, y = q.popleft()
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                    if tomato[nz][nx][ny] == 0:
                        q.append((nz, nx, ny))
                        tomato[nz][nx][ny] = tomato[z][x][y] + 1

    m, n, h = map(int, input().split())
    tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    bfs()

    res = False
    days = -2
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 0:
                    res = True
                days = max(days, tomato[k][i][j])

    if res:
        print(-1)
    elif days == 1:
        print(0)
    else:
        print(days-1)

_7569()

# days = 0
# for k in range(h):
#     for i in range(n):
#         for j in range(m):
#             if tomato[k][i][j] == 0:
