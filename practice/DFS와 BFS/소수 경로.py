from collections import deque

prime = [True for i in range(10001)]
for i in range(2, 101):
    if prime[i]:
        j = i * 2
        while j < 10001:
            prime[j] = False
            j += i
def bfs():
    q = deque()
    q.append([a, 0])
    visit = [0 for i in range(10000)]
    visit[a] = 1
    while q:
        num, cnt = q.popleft()
        if num == b: return cnt
        if num < 1000: continue
        for i in [1, 10, 100, 1000]:
            n = num - num % (i * 10) // i * i
            for j in range(10):
                if visit[n] == 0 and prime[n]:
                    visit[n] = 1
                    q.append([n, cnt + 1])
                n += i
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    res = bfs()
    if res == None:
        print("Impossible")
    else:
        print(res)