def _9461():
    def dp(n):
        dp = [0 for _ in range(101)]
        dp[1], dp[2], dp[3] = 1, 1, 1
        for i in range(4, 101):
            dp[i] = dp[i-2] + dp[i-3]
        return dp[n]

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(dp(n))

_9461()