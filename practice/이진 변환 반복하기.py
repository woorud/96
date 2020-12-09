def solution(s):
    change = 0
    cnt = 0
    
    
    while s != "1":
        change += 1
        cnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
    return [change, cnt]
    
    
print(solution("110010101001"))
