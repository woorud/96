from collections import deque, defaultdict
def _2644():
    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = True
        cnt = 0
        while q:
            cnt += 1
            for i in range(len(q)):
                k = q.popleft()
                if k == b:
                    return cnt-1

                for j in family[k]:
                    if visited[j] == False:
                        q.append(j)
                        visited[j] = True
        return -1

    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    visited = [False]*(n+1)
    family = defaultdict(lambda : [])
    for _ in range(m):
        x, y = map(int, input().split())
        family[x].append(y)
        family[y].append(x)

    print(bfs(a))

_2644()