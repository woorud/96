from itertools import combinations


def prime(n):
    if n < 2:
        return True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    num = []
    for i in combinations(nums, 3):
        num.append(sum(i))

    cnt = 0
    for i in num:
        if prime(i):
            cnt += 1

    return cnt


print(solution([1, 2, 3, 4]))