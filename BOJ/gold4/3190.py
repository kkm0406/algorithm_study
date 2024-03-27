# 뱀
# 구현, 자료 구조, 시뮬레이션, 덱, 큐
import sys
from collections import deque

input = sys.stdin.readline

# e, s, w, n
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir = 0  # 오른쪽 시작
time = 0
n = int(input())
k = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    arr[x][y] = 1

# 뱀의 위치를 저장할 덱
snake = deque()
snake.append([1, 1])

l = int(input())
ops = [list(input().split()) for _ in range(l)]

for i in range(l):
    x, c = ops[i]
    # 시작 시간으로부터 x초 동안 진행
    if i == 0:
        cnt = int(x)
    else:
        # 8 D, 10 D일 때, 8초 이동+방향 변환 -> 2초 후(10초) 방향 변환
        cnt = abs(int(ops[i][0]) - int(ops[i - 1][0]))
    for _ in range(cnt):
        nx, ny = snake[-1][0] + dx[dir % 4], snake[-1][1] + dy[dir % 4]
        time += 1
        if 1 <= nx <= n and 1 <= ny <= n:
            if [nx, ny] in snake:  # 자기자신의 몸과 부딪히는 경우
                print(time)
                exit()
            else:
                snake.append([nx, ny])
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                else:
                    snake.popleft()
        else:  # 벽에 부딪히는 경우
            print(time)
            exit()

    if c == "L":
        dir -= 1
        dir = dir % 4
    else:
        dir += 1
        dir = dir % 4

# 방향 변환 끝났을 때 게임이 안끝난 경우
while True:
    nx, ny = snake[-1][0] + dx[dir % 4], snake[-1][1] + dy[dir % 4]
    time += 1
    if 1 <= nx <= n and 1 <= ny <= n:
        if [nx, ny] in snake:  # 자기자신의 몸과 부딪히는 경우
            print(time)
            exit()
        else:
            snake.append([nx, ny])
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
            else:
                snake.popleft()
    else:  # 벽에 부딪히는 경우
        print(time)
        exit()
