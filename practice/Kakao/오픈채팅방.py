def solution(record):
    user = {}
    for rec in record:
        tmp = rec.split(" ")
        cmd = tmp[0]
        if cmd == "Enter" or cmd == "Change":
            id, name = tmp[1], tmp[2]
            user[id] = name

    log = []
    for rec in record:
        tmp = rec.split(" ")
        cmd = tmp[0]
        id = tmp[1]
        if cmd == "Enter":
            log.append("{}님이 들어왔습니다.".format(user[id]))
        elif cmd == "Leave":
            log.append("{}님이 나갔습니다.".format(user[id]))

    return log

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))