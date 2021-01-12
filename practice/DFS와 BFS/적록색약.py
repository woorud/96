import copy
from collections import deque

def _10026():
    def bfs(arr, visited, i, j):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        q = deque()
        q.append((i, j))
        visited[i][j] = True

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                    if arr[x][y] == arr[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True

    n = int(input())
    can = [list(input()) for _ in range(n)]
    cant = copy.deepcopy(can)
    for i in range(n):
        for j in range(n):
            if cant[i][j] == "R":
                cant[i][j] = "G"

    visited_can = [[False]*n for _ in range(n)]
    visited_cant = [[False]*n for _ in range(n)]

    cnt_can = 0
    cnt_cant = 0
    for i in range(n):
        for j in range(n):
            if visited_can[i][j] == False:
                bfs(can, visited_can, i, j)
                cnt_can += 1
            if visited_cant[i][j] == False:
                bfs(cant, visited_cant, i, j)
                cnt_cant += 1
    print(cnt_can, cnt_cant)

_10026()