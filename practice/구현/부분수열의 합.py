from itertools import combinations
def _1182():
    n, s = map(int, input().split())
    num_list = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n+1):
        for j in combinations(num_list, i):
            if sum(j) == s:
                cnt += 1
    print(cnt)
_1182()

# no module, dfs로 조합구하기
def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += num_list[idx]
    if sum == s:
        cnt += 1
    dfs(idx+1, sum-num_list[idx]) # 해당 인덱스를 포함하는 경우
    dfs(idx+1, sum) # 해당 인덱스를 포함하지 않는 경우

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
