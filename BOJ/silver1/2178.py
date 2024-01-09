# 미로 탐색
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(input().strip()) for i in range(n)]
visited = [[0] * m for i in range(n)]


def bfs(sx, sy):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == "1" and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

    print(visited[-1][-1])


bfs(0, 0)
