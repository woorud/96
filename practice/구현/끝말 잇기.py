def a():
    n = int(input())
    word = list(map(str, input().split()))

    for i in range(1, len(word)):
        if word[i-1][-1] == word[i][0]:
            continue
        else:
            return 0
    return 1

print(a())



