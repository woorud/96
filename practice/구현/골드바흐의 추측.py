def _9020():
    def prime(n):
        sieve = [False, False] + [True]*(n-1)
        for i in range(2, n+1):
            for j in range(i*i, n+1, i):
                sieve[j] = False
        return sieve

    t = int(input())
    for _ in range(t):
        n = int(input())
        x = n//2
        prime_list = prime(n)
        for i in range(x, 1, -1):
            if prime_list[i] and prime_list[n-i]:
                print(i, n-i)
                break
_9020()
