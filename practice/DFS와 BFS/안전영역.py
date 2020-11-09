from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and wet[nx][ny] == False:
                wet[nx][ny] = True
                q.append((nx, ny))

n = int(input())
area = [list(map(int, input().split())) for i in range(n)]
max_cnt = 0
for i in range(101):
    wet = [[False]*n for i in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if area[j][k] <= i:
                wet[j][k] = True
    for j in range(n):
        for k in range(n):
            if wet[j][k] == False:
                wet[j][k] = 1
                bfs(j, k)
                cnt += 1

    if cnt == 0:
        break
    max_cnt = max(cnt, max_cnt)
print(max_cnt)
