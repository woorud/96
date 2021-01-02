from itertools import combinations
def _6603():
    while True:
        t = list(map(int, input().split()))
        if t[0] == 0:
            return
        k, lotto = t[0], t[1:]
        for i in sorted(combinations(lotto, 6)):
            for j in i:
                print(j, end = " ")
            print()
        print()

_6603()

## DFS로 Combination 해결
def _6603():
    def DFS(start, depth):
        if depth == 6:
            for i in range(6):
                print(comb[i], end = " ")
            print()
            return
        for i in range(start, len(s)):
            comb[depth] = s[i]
            DFS(i+1, depth+1)

    comb = [0 for _ in range(13)]
    while True:
        s = list(map(int, input().split()))
        if s[0] == 0:
            break
        del s[0]
        DFS(0, 0)
        print()
