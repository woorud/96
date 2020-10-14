import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

res = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    t = heapq.heappop(heap)

    s = a + t
    res += s
    heapq.heappush(heap, s)

print(res)