from collections import deque

def _4963():
    def bfs(i, j):
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]
        q = deque()
        q.append((i, j))

        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = 0

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        maps = [list(map(int, input().split())) for _ in range(h)]

        island = 0
        for i in range(h):
            for j in range(w):
                if maps[i][j] == 1:
                    island += 1
                    bfs(i, j)

        print(island)

_4963()
