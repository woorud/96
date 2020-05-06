n = int(input())
triangle = [list(map(int, input().split())) for i in range(n)]
dp = [[0]*i for i in range(1, n+1)]
dp[0][0] = triangle[0][0]

for i in range(n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j < i:
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
        else:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
print(max(dp[-1]))