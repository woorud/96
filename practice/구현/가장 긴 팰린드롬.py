def p(s):
    if s == s[::-1]:
        return True

def solution(s):
    m = 0
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            cur = s[i:j]
            if p(cur):
                if m < len(cur):
                    m = len(cur)
    return m
