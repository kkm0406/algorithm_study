# [HSAT 7회 정기 코딩 인증평가 기출] 순서대로 방문하기

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
coords = [list(map(int, input().split())) for _ in range(m)]
for i in range(len(coords)):
    coords[i][0] -= 1
    coords[i][1] -= 1
visited = [[False] * n for _ in range(n)]
sx, sy = coords[0][0], coords[0][1]

visited[sx][sy] = True
result = 0


def dfs(idx, x, y):
    global result
    if coords[idx][0] == x and coords[idx][1] == y:
        if idx == m - 1:
            result += 1
            return
        dfs(idx + 1, x, y)

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                dfs(idx, nx, ny)
                visited[nx][ny] = False


dfs(1, sx, sy)
print(result)
