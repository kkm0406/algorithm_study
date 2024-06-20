# 지름길
# 다이나믹 프로그래밍, 그래프 이론, 데이크스트라, 최단 경로
import heapq
import sys
input = sys.stdin.readline

n, d = map(int, input().split())
arr = [[] for _ in range(10001)]
distance = [sys.maxsize]*10001

# 지름길 없이 바로 가는 경우
# i에서 i+1까지 최단거리는 1
for i in range(d+1):
    arr[i].append([i+1, 1])


for _ in range(n):
    s, e, c = map(int, input().split())
    arr[s].append([e, c])


# 다익스트라 알고리즘 사용
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in arr[now]:
            cost = dist + next[1]

            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, [cost, next[0]])


dijkstra(0)

print(distance[d])