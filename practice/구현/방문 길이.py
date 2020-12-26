def solution(dirs):
    
    d = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
    route = set()
    cx, cy = 0, 0

    for i in dirs:
        nx, ny = cx + d[i][0], cy + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            route.add((cx, cy, nx, ny))
            route.add((nx, ny, cx, cy))
            cx, cy = nx, ny            
    return len(route) // 2
