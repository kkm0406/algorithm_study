# 탈출
# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
forest = [list(input().strip()) for _ in range(r)]
dx, dy = 0, 0
sx, sy = 0, 0
dir = ((1, 0), (-1, 0), (0, -1), (0, 1))
init_water = []
for i in range(r):
    for j in range(c):
        if forest[i][j] == 'D':
            dx, dy = i, j
        if forest[i][j] == "S":
            sx, sy = i, j

visited = [[0] * c for _ in range(r)]


def flood():
    water = []
    for i in range(r):
        for j in range(c):
            if forest[i][j] == "*":
                water.append([i, j])

    for i, j in water:
        for dirx, diry in dir:
            nx = i + dirx
            ny = j + diry
            if 0 <= nx < r and 0 <= ny < c:
                if forest[nx][ny] == ".":
                    forest[nx][ny] = "*"


def bfs(sx, sy):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1
    while q:
        flood()  # 홍수 먼저나면 고슴도치 이동
        for _ in range(len(q)):  # 홍수 이후 한 턴동안 고슴도치의 다음 위치
            x, y = q.popleft()

            for dirx, diry in dir:
                nx, ny = x + dirx, y + diry
                if 0 <= nx < r and 0 <= ny < c:
                    if forest[nx][ny] == "." and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])
                    if forest[nx][ny] == "D":
                        print(visited[x][y])
                        exit()

    print("KAKTUS")


bfs(sx, sy)
