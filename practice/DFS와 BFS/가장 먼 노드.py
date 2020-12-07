from collections import deque, defaultdict
def bfs(v, visited, adj):
  cnt = 0
  q = deque()
  q.append([v, cnt])
  while q:
    v, cnt = q.popleft()
    if visited[v] == -1:
      visited[v] = cnt
      cnt += 1
      for i in adj[v]:
        q.append([i, cnt])


def solution(n, edge):
  res = 0
  visited = [-1]*(n+1)

  d = defaultdict(list)
  for i in range(len(edge)):
    d[edge[i][0]].append(edge[i][1])
    d[edge[i][1]].append(edge[i][0])
  bfs(1, visited, d)
  for i in visited:
    if i == max(visited):
      res += 1


  return res


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
