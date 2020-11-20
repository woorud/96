from collections import deque
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps[0])
    m = len(maps)
    def bfs(i, j, cnt):
        q = deque()
        q.append((i, j, cnt))
        while q:
            y, x, c = q.popleft()
            maps[y][x] = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny == m-1 and nx == n-1:
                    return c + 1

                elif 0 <= ny < m and 0 <= nx < n and maps[ny][nx] == 1:
                    maps[ny][nx] = 0
                    q.append((ny, nx, c+1))
        return -1

    return bfs(0, 0, 1)



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))