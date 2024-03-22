# 연구소
# 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0
tmp = []
virus = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            tmp.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])

# 벽을 세울 수 있는 좌표 조합
combs = list(combinations(tmp, 3))

for comb in combs:
    # 지도 복사
    arr = deepcopy(board)
    # 벽세우기
    for c in comb:
        arr[c[0]][c[1]] = 1
    # 바이러스 좌표를 큐에 집어넣음
    q = deque(virus)
    # bfs 시작
    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    q.append([nx, ny])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1

    result = max(result, cnt)

print(result)
