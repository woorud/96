from collections import deque

def bfs(v):
    q = deque()
    cnt = 0
    q.append((v, 0))
    visited = [False for i in range(n + 1)]
    visited[v] = True

    while q:
        x, c = q.popleft()
        cnt += c
        for i in tree[x]:
            if not visited[i]:
                visited[i] = True
                q.append((i, c+1))
    return cnt

n, m = map(int, input().split())
tree = [[]*i for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

answer = []
for i in range(1, n+1):
    answer.append(bfs(i))


print(answer.index(min(answer))+1)

