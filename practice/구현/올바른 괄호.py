def solution(s):
    state = 0
    for i in s:
        if i == "(":
            state += 1
        else:
            state -= 1
        if state < 0:
            return False
    if state == 0:
        return True
    else:
        return False
