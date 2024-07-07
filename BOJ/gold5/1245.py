# 농장 관리
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]


def bfs(r, c):
    visited[r][c] = True
    q = deque([[r, c]])
    h = arr[r][c] # bfs 시작점의 높이
    flag = True

    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # 미방문 정점이 높이가 같다면 탐색 진행
                if not visited[nx][ny] and arr[nx][ny] == h:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                # 시작점보다 높은 지점 발견 -> 봉우리 아님
                elif arr[nx][ny] > h:
                    flag = False

    return flag


result = 0
for r in range(n):
    for c in range(m):
        if not visited[r][c] and bfs(r, c):
            result += 1

print(result)