def solution(n):
    tile = [0] * (n+1)
    tile[0] = 1
    x = 0
    for i in range(2, len(tile)+1, 2):
        tile[i] = tile[i-2] * 3 + x*2
        x += tile[i - 2]
    return tile[-1] % 1000000007

print(solution(4))