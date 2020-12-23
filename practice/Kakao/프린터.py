from collections import deque
def solution(priorities, location):
    q = deque()
    for a, b in enumerate(priorities):
        q.append((b, a))
    
    res = 0
    while q:
        cur = q.popleft()
        
        if q and max(q)[0] > cur[0]:
            q.append(cur)
        else:
            res += 1
            if cur[1] == location:
                break
                
        
                
    return res
