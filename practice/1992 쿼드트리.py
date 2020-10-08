def quadtree(x, y, n):
    global matrix, answer
    flag = False
    check = matrix[x][y]

    for i in range(x, x+n):
        if flag:
            break
        for j in range(y, y+n):
            if matrix[j][i] != check:
                answer += '('
                quadtree(x, y, n//2)
                quadtree(x, y+n//2, n//2)
                quadtree(x+n//2, y, n//2)
                quadtree(x+n//2, y+n//2, n//2)
                answer += ')'
                flag = True
    if not flag:
        if matrix[y][x] == 1:
            answer += '1'
        else:
            answer += '0'


n = int(input())
matrix = []
answer = ''
for i in range(n):
    matrix.append(list(map(int, str(input()))))
quadtree(0, 0, n)
print(answer)
