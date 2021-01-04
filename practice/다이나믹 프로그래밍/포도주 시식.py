def _2156():
    n = int(input())
    wine = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(n+1)]
    dp[1] = wine[0]
    if n>1:
        dp[2] = wine[0] + wine[1]

    for i in range(3, n+1):
        a = wine[i-1] + dp[i-2]
        b = wine[i-1] + wine[i-2] + dp[i-3]
        c = dp[i-1]
        m = max(a, b, c)
        dp[i] = m
    print(dp[n])

_2156()