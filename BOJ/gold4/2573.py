# 빙산
# 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dir = ((1, 0), (-1, 0), (0, 1), (0, -1))
time = 0


def melt():
    coords = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                cnt = 0
                for dx, dy in dir:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                        cnt += 1
                if cnt > 0:
                    coords.append([i, j, cnt])
    return coords


def bfs(i, j, visited):
    visited[i][j] = True
    q = deque([[i, j]])
    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny] > 0:
                    q.append([nx, ny])
                    visited[nx][ny] = True


while True:
    time += 1
    coords = melt()

    for x, y, cnt in coords:
        arr[x][y] = 0 if arr[x][y] - cnt <= 0 else arr[x][y] - cnt

    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] > 0:
                bfs(i, j, visited)
                cnt += 1

    if cnt >= 2:
        print(time)
        break

    result = 0
    for i in arr:
        result += sum(i)

    if result == 0:
        print(0)
        break
