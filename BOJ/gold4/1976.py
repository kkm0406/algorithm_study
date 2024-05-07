# 여행 가자
# 자료 구조, 그래프 이론, 그래프 탐색, 분리 집합
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
visited = [False] * (n + 1)
city = [[] for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            city[i + 1].append(j + 1)


# bfs로 시작점으로부터 갈 수 있는 도시 탐색
def bfs(start):
    visited[start] = True
    q = deque([start])
    while q:
        node = q.popleft()

        for next in city[node]:
            if not visited[next]:
                q.append(next)
                visited[next] = True


bfs(plan[0])
# 여행할 도시들을 모두 방문했으면
# 계획 성공
for i in plan:
    if not visited[i]:
        print("NO")
        break
else:
    print("YES")
