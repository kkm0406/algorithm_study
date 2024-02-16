# 최소비용 구하기
# 그래프 이론, 데이크스트라, 최단 경로
import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
city = [[] for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    city[a].append([b, c])

s, e = map(int, input().split())
inf = sys.maxsize
# 시작점부터 각 노드까지 최단 거리 리스트
dist = [inf] * (n + 1)


def dijkstra(s):
    q = []
    # 단계마다 방문하지 않는 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 heap 사용
    heapq.heappush(q, [0, s])
    dist[s] = 0

    while q:
        cost, now = heapq.heappop(q)

        # 현재 노드까지의 거리보다 최단 거리 리스트에 저장된 비용이 더 작은 경우
        # -> 이미 처리된 노드
        if dist[now] < cost:
            continue

        # 다음 노드, 비용
        for next, d in city[now]:
            # 다음 노드의 비용이 현재 꺼낸 노드를 거쳐가는 비용보다 큰 경우
            if dist[next] > cost + d:
                # 비용 초기화
                dist[next] = cost + d
                heapq.heappush(q, [cost + d, next])


dijkstra(s)
print(dist[e])
