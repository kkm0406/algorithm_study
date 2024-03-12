# 최단경로
# 그래프 이론, 데이크스트라, 최단 경로
import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
arr = [[] for _ in range(v + 1)]
k = int(input())
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

inf = sys.maxsize
distance = [inf] * (v + 1)


def dijkstra(k):
    distance[k] = 0
    q = []
    heapq.heappush(q, (0, k))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, cost in arr[now]:
            if dist + cost < distance[next]:
                distance[next] = dist + cost
                heapq.heappush(q, (dist + cost, next))


dijkstra(k)

for i in range(1, v+1):
    print(distance[i] if distance[i] != inf else "INF")