def _11722():
    n = int(input())
    num_list = list(map(int, input().split()))
    dp = [1 for i in range(n)]

    for i in range(1, n):
        tmp = []
        for j in range(i):
            if num_list[i] < num_list[j]:
                tmp.append(dp[j])
        if tmp:
            dp[i] += max(tmp)
    print(max(dp))
_11722()