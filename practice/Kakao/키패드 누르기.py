def solution(numbers, hand):
    key = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]

    h = {}
    for i in range(4):
        for j in range(3):
            if j == 0:
                h[key[i][j]] = [i, j]
            elif j == 1:
                h[key[i][j]] = [i, j]
            else:
                h[key[i][j]] = [i, j]

    l = '*'
    r = '#'
    res = ''
    for i in numbers:
        if h[i][1] == 0:
            res += 'L'
            l = i
        elif h[i][1] == 2:
            res += 'R'
            r = i
        else:
            dl = abs(h[l][0] - h[i][0]) + abs(h[l][1] - h[i][1])
            dr = abs(h[r][0] - h[i][0]) + abs(h[r][1] - h[i][1])

            if dl > dr:
                res += 'R'
                r = i
            elif dl < dr:
                res += 'L'
                l = i
            else:
                if hand == 'right':
                    res += 'R'
                    r = i
                else:
                    res += 'L'
                    l = i
    return res



print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))