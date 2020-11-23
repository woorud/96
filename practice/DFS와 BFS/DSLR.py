from collections import deque
def bfs():
    q = deque()
    q.append((a, ""))
    while q:
        n, res = q.popleft()
        dn = (n*2) % 10000
        if dn == b:
            return res + "D"
        else:
            if visited[dn] == 0:
                visited[dn] = 1
                q.append((dn, res + "D"))

        if n != 0:
            sn = n-1
        else:
            sn = 9999
        if sn == b:
            return res + "S"
        else:
            if visited[sn] == 0:
                visited[sn] = 1
                q.append((sn, res + "S"))

        ln = int(n % 1000 * 10 + n / 1000)
        if ln == b:
            return res + "L"
        else:
            if visited[ln] == 0:
                visited[ln] = 1
                q.append((ln, res + "L"))

        rn = int(n % 10 * 1000 + n // 10)
        if rn == b:
            return res + "R"
        else:
            if visited[rn] == 0:
                visited[rn] = 1
                q.append((rn, res + "R"))




t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    visited = [0 for i in range(10000)]
    print(bfs())

