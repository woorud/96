import sys
def _1676():

    n = int(sys.stdin.readline())
    f = 1
    for i in range(n, 0, -1):
        f *= i


    cnt = 0
    for i in str(f)[::-1]:
        if i == '0':
            cnt += 1
        else:
            break
    print(cnt)

_1676()