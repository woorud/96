def solution(n, words):

    used = [words[0]]
    answer = [0, 0]
    for i in range(1, len(words)):
        if words[i][0] != used[-1][-1] or words[i] in used:
            answer[0] = (i%n)+1
            answer[1] = (i//n)+1
            break
        used.append(words[i])
    return answer




print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))