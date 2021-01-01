def _9095():
    t = int(input())
    for i in range(t):
        n = int(input())
        dp = [0 for _ in range(12)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for j in range(4, 12):
            dp[j] = dp[j-3] + dp[j-2] + dp[j-1]
        print(dp[n])

_9095()