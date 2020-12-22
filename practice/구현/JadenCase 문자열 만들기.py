def solution(s):
    s = list(s.lower())
    res = ""

    while s:
        cur = s.pop(0)
        try:
            int(cur)
        except:
            if len(res) == 0 or res[-1] == " ":
                cur = cur.upper()
        res += cur

    return res


print(solution("3people unFollowed me"))
print(solution("for   the last week"))