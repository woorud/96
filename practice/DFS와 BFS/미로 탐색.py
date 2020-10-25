from collections import deque
n, m = map(int, input().split())
matrix = [list(input()) for i in range(n)]
visited = [[False]*m for i in range(n)]
d = [[0]*m for i in range(n)]
q = deque()
q.append((0, 0))
visited[0][0] = True
d[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if matrix[nx][ny] == "1" and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                d[nx][ny] = d[x][y] + 1
print(d[n-1][m-1])
