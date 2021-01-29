def solution(n):
    def hanoi(n, start, to, end):
        if n == 1:
            answer.append([start, to])
        else:
            hanoi(n-1, start, end, to)
            answer.append([start, to])
            hanoi(n-1, end, to, start)

    answer = []
    hanoi(n, 1, 3, 2)
    return answer

print(solution(2))