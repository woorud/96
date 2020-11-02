def match(users, bans):
    for i in range(len(users)):
        if len(users[i]) != len(bans[i]):
            return False
        for j in range(len(users[i])):
            if bans[i][j] == "*":
                continue
            elif users[i][j] != bans[i][j]:
                return False
    return True

from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    users = permutations(user_id, len(banned_id))
    for perm in users:
        if match(perm, banned_id):
            perm = set(perm)
            if perm not in answer:
                answer.append(perm)

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"]))