import sys
def _1987():
    global max_d
    def bfs(i, j):
        global max_d

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        q = set([(i, j, arr[i][j])])

        while q:
            x, y, alpha = q.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in alpha:
                    q.add((nx, ny, alpha+arr[nx][ny]))
                    max_d = max(max_d, len(alpha)+1)

    r, c = map(int, sys.stdin.readline().split())
    arr = [list(sys.stdin.readline()) for _ in range(r)]
    max_d = 1
    bfs(0, 0)
    print(max_d)

_1987()

