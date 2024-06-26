# 톱니바퀴
# 구현, 시뮬레이션
import sys
from collections import deque

input = sys.stdin.readline

gear = [[]] + [list(input().strip()) for _ in range(4)]
for i in range(1, 5):
    gear[i] = deque(gear[i])

k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    orgin_dir = dir # num번 기어의 회전 방향
    # 맞닿은 극이 다르면 dir과 반대방향 회전
    # 같으면 동일

    # num 기어가 회전함에 따라 회전할 기어 (기어 번호, 방향)
    arr = []
    # 1번 기어가 돌아가는 경우
    if num == 1:
        # 오른쪽 방향으로만 탐색하며 회전할 기어 찾음
        for i in range(num, 4):
            # i번째 기어의 2번째 톱니와
            # i+1번째 기어의 6번째 톱니 비교
            if gear[i][2] != gear[i + 1][6]:
                dir = -dir
                arr.append([i + 1, dir])
            else:
                break
    elif num == 4:
        # 왼쪽 방향으로만 탐색
        for i in range(num, 1, -1):
            if gear[i][6] != gear[i - 1][2]:
                dir = -dir
                arr.append([i - 1, dir])
            else:
                break
    else:
        # 양방향 탐색
        dir_r, dir_l = dir, dir
        for i in range(num, 4):
            if gear[i][2] != gear[i + 1][6]:
                dir_r = -dir_r
                arr.append([i + 1, dir_r])
            else:
                break
        for i in range(num, 1, -1):
            if gear[i][6] != gear[i - 1][2]:
                dir_l = -dir_l
                arr.append([i - 1, dir_l])
            else:
                break

    # num번째 기어 회전
    gear[num].rotate(orgin_dir)
    # 나머지 기어도 따라 회전
    for idx, d in arr:
        gear[idx].rotate(d)


result = 0
for i in range(1, 5):
    if gear[i][0] == '0':
        continue
    else:
        result = result + (2 ** (i - 1))

print(result)
