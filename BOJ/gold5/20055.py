# 컨베이어 벨트 위의 로봇
# 구현, 시뮬레이션
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
# 회전 -> deque 사용
arr = deque(arr)
robot = deque([0] * n)
idx = 0

while True:
    # 벨트와 로봇 회전
    arr.rotate(1)
    robot.rotate(1)
    # 내리는 칸이면 로봇 내림
    robot[-1] = 0

    # 벨트 위에 로봇이 있으면
    if sum(robot):
        # 역순으로 탐색
        for i in range(n - 2, -1, -1):
            # 현재 로봇이 이동할 다음 칸에 로봇이 없고 벨트 내구도 1 이상이면
            if robot[i] == 1 and arr[i + 1] > 0 and robot[i + 1] == 0:
                # 한 칸 오른쪽 이동
                robot[i + 1] = 1
                # 기존 칸에서 로봇 지움
                robot[i] = 0
                # 이동한 칸 내구도 -1
                arr[i + 1] -= 1
        # 내리는 칸에 있는 로봇 내리기
        robot[-1] = 0

    # 올리는 칸에 올릴 수 있으면
    if arr[0] > 0 and robot[0] == 0:
        robot[0] = 1
        arr[0] -= 1

    idx += 1

    # 내구도가 0인 칸 개수가 k 이상이면
    if arr.count(0) >= k:
        print(idx)
        break
