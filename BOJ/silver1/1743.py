# 음식물 피하기
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [["."] * m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = "#"


def bfs(i, j):
    visited[i][j] = True
    cnt = 1
    q = deque([[i, j]])

    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == "#":
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    cnt += 1

    return cnt


result = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == "#" and not visited[i][j]:
            result = max(result, bfs(i, j))

print(result)
