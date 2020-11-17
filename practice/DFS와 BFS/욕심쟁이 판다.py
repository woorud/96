k = int(input())
tree = [list(map(int, input().split())) for _ in range(k)]
dp = [[-1 for _ in range(k)] for _ in range(k)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    dp[x][y] = 0
    day = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < k and 0 <= ny < k:
            if tree[nx][ny] > tree[x][y]:
                if dp[nx][ny] == -1:
                    dfs(nx, ny)
                day.append(dp[nx][ny])

    if day:
        dp[x][y] = max(day) + 1
    else:
        dp[x][y] = 1

res = 0
for i in range(k):
    for j in range(k):
        if dp[i][j] == -1:
            dfs(i, j)

for i in dp:
    res = max(res, max(i))
print(res)

