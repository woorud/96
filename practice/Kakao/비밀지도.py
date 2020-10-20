def solution(n, arr1, arr2):
    res = []
    for i in range(n):
        b1 = bin(arr1[i])[2:]
        b2 = bin(arr2[i])[2:]
        if len(b1) < n:
            b1 = "0" * (n - len(b1)) + b1
        if len(b2) < n:
            b2 = "0" * (n - len(b2)) + b2

        tmp = ""
        for j in range(n):
            if b1[j] == "1" or b2[j] == "1":
                tmp += "#"
            else:
                tmp += " "
        res.append(tmp)
    return res

print(solution(5, 	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))