from collections import deque


def bfs(i, j):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < h and ny < w and graph[nx][ny]:
                graph[nx][ny] = 0
                q.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for i in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
