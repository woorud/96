def _11399():
    n = int(input())
    line = list(map(int, input().split()))
    people = []
    for i in range(len(line)):
        time = [i + 1, line[i]]
        people.append(time)
    people = sorted(people, key=lambda x: (x[1], x[0]))

    time = 0
    for i in range(len(people)):
        time += people[i][1] * (n - i)

    print(time)

_11399()