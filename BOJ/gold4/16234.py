# 인구 이동
# 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, 너비 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
time = 0


def bfs(i, j):
    q = deque()
    q.append([i, j])
    countries = set()
    countries.add((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 조건충족하면
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    # 국경을 공유하는 나라 리스트
                    countries.add((nx, ny))

    return countries


while True:
    visited = [[False] * n for _ in range(n)]
    flag = False # 인구 이동 여부
    for i in range(n):
        for j in range(n):
            # 미방분 나라면
            if not visited[i][j]:
                visited[i][j] = True
                # bfs로 주변 나라 탐색
                countries = bfs(i, j)
                if len(countries) > 1:
                    flag = True
                    people = 0
                    for c in countries:
                        people += arr[c[0]][c[1]]
                    people = people // len(countries)

                    for c in countries:
                        arr[c[0]][c[1]] = people
    if not flag:
        break
    time += 1

print(time)
