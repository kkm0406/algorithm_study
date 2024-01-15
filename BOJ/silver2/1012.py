# 유기농 배추
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j):
    q = deque([[i, j]])
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = True


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
