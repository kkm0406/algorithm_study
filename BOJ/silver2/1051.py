# 숫자 정사각형
# 구현, 브루트포스 알고리즘

import sys

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
result = []
for i in range(n):
    for j in range(m):
        # 정사각형 시작위치
        sx, sy = i, j
        flag = False
        target = arr[sx][sy]
        # 시작위치에서 움직일 칸
        move = 0
        # 가장 많이 움직인 칸
        idx = 0
        # 가로, 세로 끝까지 이동할 때
        while sx + move < n and sy + move < m:
            # 이동한 칸의 값이 target과 같으면
            if arr[sx + move][j] == arr[sx][sy + move] == arr[sx + move][sy + move] == target:
                idx = max(move, idx)
            # 한 칸 이동
            move += 1
        result.append(idx)

# 이동칸+1를 제곱 (정사각형이 1인 경우 max(result)가 0)
print((max(result) + 1) ** 2)
