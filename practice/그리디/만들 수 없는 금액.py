n = int(input())
coin = list(map(int, input().split()))
coin.sort()

res = 1
for i in coin:
    if res < i:
        break
    res += i

print(res)