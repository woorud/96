from collections import deque, defaultdict
def _2606():
    def bfs(x):
        q = deque()
        q.append(x)
        visited[x] = True
        cnt = 0
        while q:
            cnt += 1
            z = q.popleft()
            for i in d[z]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
        return cnt-1


    n = int(input())
    m = int(input())
    d = defaultdict(lambda:[])
    for i in range(m):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    visited = [False]*(n+1)
    print(bfs(1))




_2606()