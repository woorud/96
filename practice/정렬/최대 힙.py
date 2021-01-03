import heapq
import sys
def _11279():
    s = list()
    heapq.heapify(s)
    n = int(input())
    for i in range(n):
        x = int(sys.stdin.readline())
        if x != 0:
            heapq.heappush(s, -x)
        else:
            if len(s) == 0:
                print(0)
            else:
                print(-1*heapq.heappop(s))


_11279()