from collections import deque
def bfs(v):
    q = deque()
    q.append((v))
    visited = [False for _ in range(n+1)]
    visited[v] = True
    cnt = 1
    while q:
        x = q.popleft()
        for i in trust[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt

n, m = map(int, input().split())
trust = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    trust[b].append(a)

res = []
m = -1
for i in range(1, n+1):
    tmp = bfs(i)
    if tmp > m:
        m = tmp
        res = [i]
    elif tmp == m:
        res.append(i)
        m = tmp

for i in res:
    print(i, end = ' ')