# 플로이드
# 그래프 이론, 최단 경로, 플로이드-워셜
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
# dist[i][j] = c -> i에서 j로 갈 때 c 비용
# 일단 1e9로 초기화
dist = [[1e9] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        # 시작 도시와 도착 도시가 같은 경우
        if i == j:
            dist[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # 시작 도시, 도착 도시는 같지만 비용이 다른 경우도 있음
    if dist[a - 1][b - 1] > c:
        dist[a - 1][b - 1] = c

for i in range(n):
    for j in range(n):
        for k in range(n):
            # j도시에서 k도시로 갈 때 i도시를 거치는 경우의 비용이 더 적게 나갈 때
            if dist[j][i] + dist[i][k] < dist[j][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

for i in range(n):
    for j in range(n):
        if dist[i][j] == 1e9:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()