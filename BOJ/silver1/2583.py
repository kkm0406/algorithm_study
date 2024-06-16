# 영역 구하기
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [[0] * m for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 1

visited = [[False] * m for _ in range(n)]
size = []


def bfs(r, c):
    visited[r][c] = True
    q = deque()
    q.append([r, c])
    cnt = 1
    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1

    return cnt

for r in range(n):
    for c in range(m):
        if not visited[r][c] and arr[r][c] == 0:
            size.append(bfs(r, c))

print(len(size))
print(*sorted(size))