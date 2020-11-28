import heapq
def solution(food_times, k):
    food_times = [(food, idx+1) for idx, food in enumerate(food_times)]

    heapq.heapify(food_times)

    small = food_times[0][0]
    prev = 0
    while k - ((small-prev)*len(food_times)) >= 0:
        k -= (small-prev)*len(food_times)
        prev, idx = heapq.heappop(food_times)
        if not food_times:
            return -1
        small = food_times[0][0]
    food_times = sorted(food_times, key=lambda x:x[1])
    return food_times[k%len(food_times)][1]



print(solution([3, 1, 2], 5))