# 단지번호붙이기
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
house = []
arr = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    cnt = 1
    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] == '1':
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1

    return cnt


for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == '1':
            house.append(bfs(i, j))


print(len(house))
for i in sorted(house):
    print(i)
