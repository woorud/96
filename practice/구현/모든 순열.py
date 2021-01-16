def _10974():
    def permutations(visited, cnt):
        if cnt == n:
            print(' '.join(list(map(str, visited))))
        else:
            for i in range(1, n+1):
                if i not in visited:
                    permutations(visited+[i], cnt+1)

    n = int(input())
    visited = []
    permutations(visited, 0)

_10974()