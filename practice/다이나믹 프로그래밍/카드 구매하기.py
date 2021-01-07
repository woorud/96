def _11052():
    n = int(input())
    card = [0] + list(map(int, input().split()))
    dp = [0] * (n+1)
    dp[1] = card[1]
    dp[2] = max(2*card[1], card[2])
    for i in range(3, n+1):
        dp[i] = card[i]
        for j in range(1, i//2+1):
            dp[i] = max(dp[i], dp[j]+dp[i-j])
    print(dp[-1])

_11052()