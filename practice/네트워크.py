def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            tmp = stack.pop()
            if visited[tmp] == 0:
                visited[tmp] = 1
            for i in range(len(computers)):
                if computers[tmp][i] == 1 and visited[i] == 0:
                    stack.append(i)
    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))