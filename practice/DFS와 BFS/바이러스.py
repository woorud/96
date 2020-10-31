n = int(input())
p = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(p):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(now_pos):
    global cnt
    cnt += 1
    visited[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)

dfs(1)
print(cnt-1)
