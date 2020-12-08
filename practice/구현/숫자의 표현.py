def solution(n):
    res = 0
    for i in range(1, n):
        tmp = i
        for j in range(i+1, n):
            tmp += j
            if tmp == n:
                res += 1
                break
            elif tmp > n:
                break
    return res+1
