from collections import deque
def _2583():
    def bfs(i, j):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()
        q.append((i, j))
        area[i][j] = 1
        s = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and area[nx][ny] == 0:
                    q.append((nx, ny))
                    area[nx][ny] = 1
                    s += 1
        return s


    m, n, k = map(int, input().split())
    area = [[0]*n for _ in range(m)]
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        for i in range(b, d):
            for j in range(a, c):
                area[i][j] = 1

    res = []
    for i in range(m):
        for j in range(n):
            if area[i][j] == 0:
                res.append(bfs(i, j))

    print(len(res))
    for i in sorted(res):
        print(i, end = ' ')
_2583()