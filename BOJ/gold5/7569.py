# 토마토
# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = []
for _ in range(h):
    tmp = [list(map(int, input().split())) for i in range(n)]
    arr.append(tmp)

tomato = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                tomato.append([j, k, i])


while tomato:
    x, y, z = tomato.popleft()

    for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        nx, ny, nz = x + dx, y + dy, z + dz

        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                tomato.append([nx, ny, nz])

result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, arr[i][j][k])

print(result-1)