from collections import deque
def _2667():
    def bfs(i, j):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()
        q.append((i, j))
        apt[i][j] = "0"
        cnt = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and apt[nx][ny] == "1":
                    q.append((nx, ny))
                    apt[nx][ny] = "0"
                    cnt += 1
        return cnt

    n = int(input())
    apt = [list(input()) for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if apt[i][j] == "1":
                res.append(bfs(i, j))
    print(len(res))
    for i in sorted(res):
        print(i)


_2667()