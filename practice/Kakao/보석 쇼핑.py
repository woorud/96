def solution(gems):
    start, end = 0, 0
    gn = len(set(gems))
    gd = {gems[0]:1}
    res = (0, 100001)

    while start < len(gems) and end < len(gems):
        if len(gd) < gn:
            if end == len(gems) - 1:
                break
            end += 1
            if gems[end] not in gd:
                gd[gems[end]] = 1
            else:
                gd[gems[end]] += 1
        else:
            if end - start < res[1] - res[0]:
                res = [start+1, end+1]
            if gd[gems[start]] == 1:
                del gd[gems[start]]
            else:
                gd[gems[start]] -= 1
            start += 1
    return res

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
