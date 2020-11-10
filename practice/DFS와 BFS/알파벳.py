import sys
def BFS(x, y):
    global answer

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = set([(x, y, alpha[x][y])])

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ((0 <= nx < R) and (0 <= ny < C)) and (alpha[nx][ny] not in ans):
                q.add((nx, ny, ans + alpha[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
alpha = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)