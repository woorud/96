def solution(n):

    res = ""
    while n > 0:
        n -= 1
        res = "124"[n%3] + res
        n //= 3
    return res

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))
print(solution(11))
