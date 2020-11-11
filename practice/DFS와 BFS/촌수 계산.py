from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    ans = 0
    while q:
        ans += 1
        for i in range(len(q)):
            k = q.popleft()
            if k == b:
                return ans-1
            for j in tree[k]:
                if visited[j] == False:
                    visited[j] = True
                    q.append(j)

    return -1

n = int(input())
a, b = map(int ,input().split(' '))
m = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split(' '))
    tree[x].append(y)
    tree[y].append(x)

visited = [False] * (n+1)
print(bfs(a))