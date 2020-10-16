def solution(dartResult):
    res = []
    n = ''
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == "S":
            res.append(int(n) ** 1)
            n = ''
        elif i == "D":
            res.append(int(n) ** 2)
            n = ''
        elif i == "T":
            res.append(int(n) ** 3)
            n = ''
        elif i == "#":
            res[-1] = res[-1] * -1
        elif i == "*":
            if len(res) > 1:
                res[-2] = res[-2] * 2
            res[-1] = res[-1] * 2
    return sum(res)

print(solution("1S2D*3T"))