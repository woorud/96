def _1932():
    n = int(input())
    tri = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*i for i in range(1, n+1)]
    dp[0][0] = tri[0][0]
    dp[1][0], dp[1][1] = dp[0][0]+tri[1][0], dp[0][0]+tri[1][1]
    for i in range(2, n):
        dp[i][0] += tri[i][0] + dp[i-1][0]
        for j in range(1, i):
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]
        dp[i][i] += tri[i][i] + dp[i-1][i-1]
    print(max(dp[-1]))

_1932()
