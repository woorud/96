from collections import deque
def _11724():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = True
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
    print(cnt)


_11724()