def solution(N, stages):
    fp = []
    n = len(stages)
    for lv in range(1, N+1):
        fail = 0
        if n != 0:
            for stage in stages:
                if stage == lv:
                    fail += 1

            fp.append((lv, fail/n))
            n -= fail
        else:
            fp.append((lv, 0))

    fp = sorted(fp, key = lambda x : x[1], reverse = True)
    return [i[0] for i in fp]

print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,	[4,4,4,4,4]))