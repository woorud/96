def solution(s, n):
    
    s = list(s)
    res = ""
    for i in s:
        if i.isupper():
            tmp = chr((ord(i)-ord("A")+n)%26+ord("A"))
            res += tmp
        elif i.islower():
            tmp = chr((ord(i)-ord("a")+n)%26+ord("a"))
            res += tmp
        else:
            res += " "
            
            
    return res
