n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
minus, zero, plus = 0, 0, 0

def cut(x, y, n):
    global minus, zero, plus
    cur = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if cur != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        cut(x+k*n//3, y+l*n//3, n//3)
                return

    if cur == -1:
        minus += 1
    elif cur == 0:
        zero += 1
    elif cur == 1:
        plus += 1

cut(0, 0, n)
print("{}\n{}\n{}".format(minus, zero, plus))