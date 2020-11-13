from collections import deque
from collections import defaultdict
n = int(input())
tree = defaultdict(list)
h = [0] * (n+1)
h[1] = 1
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque([1])
while q:
    x = q.popleft()
    for i in tree[x]:
        if not h[i]:
            h[i] = x
            q.append(i)

for i in h[2:]:
    print(i)
