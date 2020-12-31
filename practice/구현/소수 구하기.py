def prime(n):
    p = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if p[i] == True:
            for j in range(2*i, n+1, i):
                p[j] = False
    return p

def _1929():
    m, n = map(int, input().split())
    p = prime(n)
    return [print(i) for i in range(2, len(p)) if p[i]==True and i >= m]

_1929()
