# 토마토
# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])


def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append([nx, ny])


bfs()
result = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        result = max(result, tomato[i][j])

print(result - 1)
