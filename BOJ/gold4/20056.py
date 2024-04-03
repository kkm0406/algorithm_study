# 마법사 상어와 파이어볼
# 구현, 시뮬레이션
import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
fireballs = deque()
for i in range(M):
    # r, c, 질량, 속력, 방향
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])

arr = [[[] for i in range(N)] for _ in range(N)]
dir = {0: [-1, 0], 1: [-1, 1], 2: [0, 1], 3: [1, 1], 4: [1, 0], 5: [1, -1], 6: [0, -1], 7: [-1, -1]}

for _ in range(K):

    while fireballs:
        # r, c, 질량, 속력, 방향
        r, c, m, s, d = fireballs.popleft()
        # 파이어볼 이동
        nr, nc = (r + dir[d][0] * s) % N, (c + dir[d][1] * s) % N
        arr[nr][nc].append([m, s, d])

    for x in range(N):
        for y in range(N):
            # 2개 이상의 파이어볼이 있는 칸
            if len(arr[x][y]) >= 2:
                # 총 질량, 속도, 방향 체크(모두 홀수/짝수인지), 합쳐진 개수
                mass, speed, d_odd, d_even, cnt = 0, 0, 0, 0, len(arr[x][y])
                while arr[x][y]:
                    tmp_m, tmp_s, tmp_d = arr[x][y].pop(0)
                    mass += tmp_m
                    speed += tmp_s
                    # 합쳐지는 파이어볼의 방향 확인
                    if tmp_d % 2 == 0:
                        d_even += 1
                    else:
                        d_odd += 1
                # 합쳐지는 파이어볼의 방향이 모두 짝수/홀수
                if d_odd == cnt or d_even == cnt:
                    if mass // 5 > 0:
                        for new_d in [0, 2, 4, 6]:
                            fireballs.append([x, y, mass // 5, speed // cnt, new_d])
                else:
                    if mass // 5 > 0:
                        for new_d in [1, 3, 5, 7]:
                            fireballs.append([x, y, mass // 5, speed // cnt, new_d])
            elif len(arr[x][y]) == 1:
                fireballs.append([x, y] + arr[x][y].pop())

result = 0
for f in fireballs:
    result += f[2]
print(result)
