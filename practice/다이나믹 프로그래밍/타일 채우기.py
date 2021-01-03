def _2133():
    n = int(input())

    dp = [0 for _ in range(31)]
    dp[0], dp[2] = 1, 3
    for i in range(4, 31, 2):
        dp[i] = dp[i-2]*3
        for j in range(i-4, -1, -2):
            dp[i] += dp[j]*2
    print(dp[n])

_2133()