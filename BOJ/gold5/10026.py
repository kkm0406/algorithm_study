# 적록색약
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = [list(input().strip()) for _ in range(n)]
cnt1, cnt2 = 0, 0
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
rgb = []
for i in arr:
    tmp = "".join(i)
    tmp = tmp.replace("R", "G")
    rgb.append(list(tmp))


def bfs(i, j, color, visited, board):
    visited[i][j] = True
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == color:
                    q.append([nx, ny])
                    visited[nx][ny] = True


for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(i, j, arr[i][j], visited1, arr)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs(i, j, rgb[i][j], visited2, rgb)
            cnt2 += 1

print(cnt1, cnt2)
