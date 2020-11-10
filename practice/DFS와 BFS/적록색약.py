from collections import deque
import copy

def bfs(vistied, i, j, arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((i, j))
    vistied[i][j] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n and vistied[nx][ny] == False:
                if arr[x][y] == arr[nx][ny]:
                    q.append((nx, ny))
                    vistied[nx][ny] = True


n = int(input())
rgb = [list(input()) for i in range(n)]
blind = copy.deepcopy(rgb)
for i in range(n):
    for j in range(n):
        if blind[i][j] == "G":
            blind[i][j] = "R"

rgb_visited = [[False]*n for i in range(n)]
blind_visited = [[False]*n for i in range(n)]

res1 = 0
res2 = 0
for i in range(n):
    for j in range(n):
        if rgb_visited[i][j] == False:
            bfs(rgb_visited, i, j, rgb)
            res1 += 1
        if blind_visited[i][j] == False:
            bfs(blind_visited, i, j, blind)
            res2 += 1
print(res1, res2)
