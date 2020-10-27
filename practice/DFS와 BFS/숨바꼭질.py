from collections import deque
n, k = map(int, input().split())
visited = [0 for i in range(100001)]

def bfs(v):
    q = deque()
    cnt = 0
    q.append((v, cnt))

    while q:
        v = q.popleft()
        a = v[0]
        cnt = v[1]
        if visited[a] == 0 and a == k:
            return cnt
        cnt += 1
        if visited[a] == 0 and a*2 <= 100000:
            q.append((a*2, cnt))
        if visited[a] == 0 and a+1 <= 100000:
            q.append((a+1, cnt))
        if visited[a] == 0 and a-1 >= 0:
            q.append((a-1, cnt))
    return cnt

print(bfs(n))
