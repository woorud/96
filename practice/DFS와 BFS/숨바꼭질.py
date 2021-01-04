from collections import deque
def _1697():
    n, k = map(int, input().split())
    array = [0 for _ in range(100001)]
    def bfs(v):
        q = deque()
        q.append(v)
        while q:
            x = q.popleft()
            if x == k:
                print(array[x])
                return
            for i in (x-1, x+1, 2*x):
                if 0 <= i < len(array) and not array[i]:
                    array[i] = array[x] + 1
                    q.append(i)
    bfs(n)

_1697()