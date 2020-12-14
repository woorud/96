from itertools import permutations


def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    num = set()
    for i in range(1, len(numbers) + 1):
        tmp = permutations(numbers, i)
        for j in tmp:
            num.add(int("".join(j)))
    num = sorted(list(num))
    cnt = 0
    for i in num:
        if prime(i):
            cnt += 1
    return cnt

print(solution("17"))
print(solution("011"))