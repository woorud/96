def _4948():

    def prime(a, b):
        sieve = [False, False] + [True] * (b-2)
        for i in range(2, b):
            if sieve[i] == True:
                for j in range(2*i, b, i):
                    sieve[j] = False
        return sieve[a:b]

    while True:
        n = int(input())
        if n == 0 :
            break
        a, b = n, 2*n
        cnt = 0
        for i in prime(a+1, b+1):
            if i == True:
                cnt += 1
        print(cnt)


_4948()