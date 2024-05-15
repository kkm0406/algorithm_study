# 치즈
# 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, 너비 우선 탐색

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cheese = 0
for i in arr:
    cheese += sum(i)
time = 0


# 외부 공기와 접촉한 치즈만 녹이려면 값이 0인 부분에 대해서만 BFS 진행
# (0, 0)에서 시작해서 상하좌우를 탐색하고 해당 지점이 0이면 공기 -> 계속 탐색
# 탐색한 지점이 1 -> 공기와 맞닾은 치즈
def bfs():
    q = deque([[0, 0]])
    melt = []
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == 0:  # 공기면 계속 탐색하기 위해 큐에 삽입
                    q.append([nx, ny])
                else:  # 공기와 맞닿은 치즈
                    melt.append([nx, ny])

    for x, y in melt:
        arr[x][y] = 0

    return len(melt)


while True:
    time += 1
    visited = [[False] * m for _ in range(n)]
    result = bfs()
    cheese -= result
    if cheese == 0:
        print(time)
        print(result)
        break
