# 뒤집기 II
# 그리디 알고리즘
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

# 초기 뒷면의 좌표
coords = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            coords.append([i, j])

# (0, 0)로부터 먼 위치의 좌표부터 순서대로 뒤집음
coords.sort(reverse=True)
coords = deque(coords)
cnt = 0
while True:
    # 모두 앞면인지 확인
    total = 0
    for i in arr:
        total += sum(i)
    if total == 0:
        break

    # (0, 0)으로부터 가장 먼 뒷면의 좌표
    r, c = coords.popleft()

    # (r, c)까지 모든 동전을 뒤집음
    for x in range(r + 1):
        for y in range(c + 1):
            if arr[x][y] == 1:
                arr[x][y] = 0
            else:
                arr[x][y] = 1

    # 뒤집기 이후 뒷면 찾기
    new_coords = []
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1:
                new_coords.append([x, y])

    # 다시 정렬
    new_coords.sort(reverse=True)
    coords = deque(new_coords)
    cnt += 1

print(cnt)
