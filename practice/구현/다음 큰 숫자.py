def solution(n):
    
    a = str(bin(n))[2:].count("1")
    
    for i in range(n+1, 1000001):
        if a == str(bin(i))[2:].count("1"):
            return i
