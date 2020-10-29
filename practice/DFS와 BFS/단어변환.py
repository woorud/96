from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque()
    q.append((begin, 0))
    visited = dict()
    visited[begin] = True
    while q:
        cur, cnt = q.popleft()
        for w in words:
            if one(cur, w) and w not in visited:
                visited[w] = True
                q.append((w, cnt+1))
                if w == target:
                    return cnt + 1

def one(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    if cnt == 1:
        return True
    return False


