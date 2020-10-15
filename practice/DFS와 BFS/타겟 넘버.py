def solution(numbers, target):
    res = [0]
    for i in numbers:
        tmp = []
        for j in res:
            tmp.append(j + i)
            tmp.append(j - i)
        res = tmp
    return res.count(target)


print(solution([1, 1, 1, 1, 1], 3))