# 소문난 칠공주
# 수학, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 조합론, 백트래킹
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
arr = [list(input().strip()) for _ in range(5)]
coords = []

for i in range(5):
    for j in range(5):
        coords.append([i, j])

# 5*5에서 좌표 7개의 조합
combs = list(combinations(coords, 7))


def check(comb):
    s = 0
    for x, y in comb:
        if arr[x][y] == "S":
            s += 1

    return s


# bfs로 해당 조합의 연결여부 확인
def isLinked(visited, comb):
    q = deque()
    # 시작점 큐에 삽입
    q.append([comb[0][0], comb[0][1]])
    visited[comb[0][0]][comb[0][1]] = True
    cnt = 1  # 연결된 학생 수
    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                # 다음에 이동할 좌표가 comb 조합에 있으면 큐에 삽입하고
                # 이어서 탐색 진행
                if [nx, ny] in comb:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1  # 연결된 학생 추가
                    if cnt == 7:  # 7명이 연결되었으면 더 이상 탐색 종료
                        return True
                # 큐에 없으면 다음 좌표 탐색
                else:
                    continue
    return False


result = 0
for comb in combs:
    visited = [[False] * 5 for _ in range(5)]

    # 다솜파가 4명 이상이고,
    # 해당 조합이 모두 연결되어 있는지 확인
    if check(comb) >= 4 and isLinked(visited, comb):
        result += 1

print(result)
