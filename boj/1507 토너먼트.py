n, a, b = map(int, input().split())
round = 0
while a != b:
    a -= a//2
    b -= b//2
    round += 1
print(round)