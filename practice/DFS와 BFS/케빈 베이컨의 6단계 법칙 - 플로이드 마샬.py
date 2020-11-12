# 플로이드 와샬 알고리즘: 모든 정점에서 모든 정점으로의 최단 경로
import sys

INF = float("inf")

n, m = map(int, sys.stdin.readline().split())

# 각 정점을 최단 거리로 초기화
relation = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())

    relation[x-1][y-1] = 1
    relation[y-1][x-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                relation[i][j] = 0
            else:
                relation[i][j] = min(relation[i][j], relation[i][k] + relation[k][j])

bacon = []
for i in relation:
    bacon.append(sum(i))
print(bacon.index(min(bacon))+1)