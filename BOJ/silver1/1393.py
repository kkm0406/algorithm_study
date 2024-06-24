# 음하철도 구구팔
# 수학, 브루트포스 알고리즘, 정수론
import math
import sys

input = sys.stdin.readline

sx, sy = map(int, input().split())
ex, ey, dx, dy = map(int, input().split())

# 1초당 x, y가 이동하는 크기
move_x = dx // math.gcd(dx, dy)
move_y = dy // math.gcd(dx, dy)


def get_dist(x, y):
    return math.sqrt((sx - x) ** 2 + (sy - y) ** 2)


# 현재 좌표에서의 거리가 다음에 움직일 좌표에서부터의 거리보다 크면
# 계속 이동하면서 거리 탐색
# 현재 좌표에서의 거리가 다음에 이동한 좌표에서의 거리보다 작으면
# 현재 좌표가 최소 거리
while True:
    if get_dist(ex, ey) < get_dist(ex + move_x, ey + move_y):
        break
    else:
        ex += move_x
        ey += move_y

print(ex, ey)
