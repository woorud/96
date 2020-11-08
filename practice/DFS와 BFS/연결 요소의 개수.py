from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        bfs(i)
        cnt += 1

sys.stdout.write(str(cnt))
