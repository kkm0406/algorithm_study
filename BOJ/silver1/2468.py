# 안전 영역
# 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
import copy
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
height = set()
result = []
for i in arr:
    for j in i:
        height.add(j)


def bfs(i, j, h, area):
    visited[i][j] = True
    q = deque([[i, j]])
    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if area[nx][ny] > h:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    area[nx][ny] = 0


for h in height:
    area = copy.deepcopy(arr)
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] > h:
                bfs(i, j, h, area)
                cnt += 1

    # for k in area:
    #     print(*k)
    # print()
    if cnt == 0:
        result.append(1)
    else:
        result.append(cnt)

print(max(result))