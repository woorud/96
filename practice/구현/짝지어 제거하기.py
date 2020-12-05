def solution(s):
    answer = 0
    s = list(s)
    arr = []

    for i in s:
        if len(arr) == 0:
            arr.append(i)
        elif arr[-1] == i:
            arr.pop()
        else:
            arr.append(i)
    if len(arr) == 0:
        return 1
    return 0


print(solution("baabaa"))
print(solution("cdcd"))