import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    s = [0 for i in range(n + 1)]
    for j in range(n):
        a, b = map(int, sys.stdin.readline().split())
        s[a] = b
    min_n = s[1]
    cnt = 0
    for k in range(2, n + 1):
        if s[k] > min_n:
            cnt += 1
        else:
            min_n = s[k]        
    print(n - cnt)
