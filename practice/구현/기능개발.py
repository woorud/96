from collections import defaultdict
def solution(progresses, speeds):

    days = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] == 0:
            day = (100-progresses[i])//speeds[i]
        else:
            day = (100-progresses[i])//speeds[i]+1

        if len(days) == 0:
            days.append(day)
        else:
            if days[-1] > day:
                days.append(days[-1])
            else:
                days.append(day)

    res = defaultdict(lambda:0)
    for i in days:
        res[i] += 1
    return [i for i in res.values()]
