from collections import defaultdict

def solution(genres, plays):
    rank = defaultdict(lambda:0)
    playing = defaultdict(lambda:[])


    for idx, gp in enumerate(zip(genres, plays)):
        rank[gp[0]] += gp[1]
        playing[gp[0]].append((idx, gp[1]))


    rank = sorted(rank.items(), key=lambda x:x[1], reverse=True)

    res = []
    for i in rank:
        s = sorted(playing[i[0]], key=lambda x:x[1], reverse=True)
        res.append(s[0][0])
        if len(s) > 1:
            res.append(s[1][0])
    return res
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))