def solution(m, musicinfos):
    m = m.replace("C#", "H")
    m = m.replace("D#", "I")
    m = m.replace("F#", "J")
    m = m.replace("G#", "K")
    m = m.replace("A#", "L")

    song = {}
    for i in musicinfos:
        s, e, name, code = i.split(",")
        start = 60 * int(s.split(":")[0]) + int(s.split(":")[1])
        end = 60 * int(e.split(":")[0]) + int(e.split(":")[1])
        playing = end - start

        code = code.replace("C#", "H")
        code = code.replace("D#", "I")
        code = code.replace("F#", "J")
        code = code.replace("G#", "K")
        code = code.replace("A#", "L")
        code = code * (playing // len(code)) + code[:playing%len(code)]

        song[code] = name

    res = None
    for s in song.keys():
        if m in s:
            if res == None:
                res = s
            else:
                if len(res) < len(s):
                    res = s
    if res != None:
        return song[res]
    else:
        return "(None)"

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))