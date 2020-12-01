def solution(N, number):
    dp = [0, {N}]
    if N == number:
        return 1
    for i in range(2, 9):
        s = {int(str(N)*i)}
        for j in range(1, i//2+1):
            for a in dp[j]:
                for b in dp[i-j]:
                    s.add(a+b)
                    s.add(a-b)
                    s.add(b-a)
                    s.add(a*b)
                    if a != 0:
                        s.add(b//a)
                    if b != 0:
                        s.add(a//b)
        if number in s:
            return i

        dp.append(s)
    return -1

print(solution(5, 12))
