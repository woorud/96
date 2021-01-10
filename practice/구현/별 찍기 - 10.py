def _2447():
    def s(arr):
        matrix = []
        for i in range(3*len(arr)):
            if i//len(arr) == 1:
                matrix.append(arr[i%len(arr)] + ' '*len(arr) + arr[i%len(arr)])
            else:
                matrix.append(arr[i%len(arr)]*3)
        return matrix

    n = int(input())
    star = ['***', '* *', '***']
    k = 0
    while n != 3:
        n //= 3
        k += 1

    for i in range(k):
        star = s(star)

    for i in star:
        print(i)

_2447()