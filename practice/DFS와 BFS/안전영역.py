from collections import deque
def _2468():
    def bfs(i, j):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()
        q.append((i, j))
        wet[i][j] = True
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and wet[nx][ny] == False:
                    q.append((nx, ny))
                    wet[nx][ny] = True


    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    res = []
    for i in range(101):
        cnt = 0
        wet = [[False]*n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if area[x][y] <= i:
                    wet[x][y] = True
        for x in range(n):
            for y in range(n):
                if wet[x][y] == False:
                    cnt += 1
                    bfs(x, y)
        res.append(cnt)
    print(max(res))


_2468()