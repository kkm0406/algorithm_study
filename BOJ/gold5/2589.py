# 보물섬
# 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
result = 0


def bfs(r, c):
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    q = deque([[r, c]])

    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == "L":
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

    cost = 0
    for i in visited:
        cost = max(cost, max(i))
    return cost


for r in range(n):
    for c in range(m):
        if board[r][c] == "L":
            result = max(result, bfs(r, c))

print(result - 1)
