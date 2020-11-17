num_list = [list(input().split()) for _ in range(5)]
res = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, num):
    if len(num) == 6:
        res.add(num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + num_list[nx][ny])


for i in range(5):
    for j in range(5):
        if num_list[i][j]:
            dfs(i, j, num_list[i][j])
print(len(res))