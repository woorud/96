n, k = map(int, input().split())

MAX = -1
dist = [-1 for i in range(100001)]

def bfs(v):
    q = [v]
    dist[v] = 0
    nxt_q = []
    while q:
        now = q.pop(0)
        if now * 2 <= 100000 and dist[now * 2] == -1:
            dist[now * 2] = dist[now]
            q.append(now * 2)
        if now + 1 <= 100000 and dist[now + 1] == -1:
            dist[now + 1] = dist[now] + 1
            nxt_q.append(now + 1)
        if now - 1 >= 0 and dist[now - 1] == -1:
            dist[now - 1] = dist[now] + 1
            nxt_q.append(now - 1)
        if not q:
            q = nxt_q
            nxt_q = []
bfs(n)
print(dist[k])
