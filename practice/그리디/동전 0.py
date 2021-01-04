def _11047():
    n, k = map(int, input().split())
    coin = [int(input()) for _ in range(n)]

    cnt = 0
    for i in range(n-1, -1, -1):
        if k == 0:
            break
        if coin[i] > k:
            continue
        cnt += k//coin[i]
        k %= coin[i]
    print(cnt)
_11047()