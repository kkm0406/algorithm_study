# 미세먼지 안녕!
# 구현, 시뮬레이션
import sys

input = sys.stdin.readline
r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
top, bottom = 0, 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    if room[i][0] == -1:
        top = i
        bottom = i + 1
        break


def fine_dust():
    # 확산될 미세먼지
    dust = []
    for x in range(r):
        for y in range(c):
            if room[x][y] > 0:
                rest = 0 # 확산된 미세먼지 수
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        # 확산될 위치와 미세먼지 양
                        dust.append([nx, ny, room[x][y] // 5])
                        rest += 1
                # 확산된 만큼 차감
                room[x][y] -= (room[x][y] // 5) * rest
    # 미세먼지 초기화
    for x, y, d in dust:
        room[x][y] += d


def air_top():
    dir = 1 # 시작 방향
    x, y = top, 1  # 시작 위치(공기청정기 다음 좌표)
    prev = 0 # prev와 바꾸면서 한 칸씩 이동
    while True:
        # 공기청정기 좌표로 오면 중단
        if x == top and y == 0:
            break
        nx, ny = x + dx[dir], y + dy[dir]
    
        # 벽에 닿으면 반시계 회전
        if nx == -1 or nx == r or ny == -1 or ny == c:
            dir = (dir - 1) % 4
            continue
        
        # 이전 값과 swap하며 이동
        room[x][y], prev = prev, room[x][y]
        x, y = nx, ny


def air_bottom():
    dir = 1
    x, y = bottom, 1  # 시작 위치
    prev = 0
    while True:
        if x == bottom and y == 0:
            break

        nx, ny = x + dx[dir], y + dy[dir]

        if nx == -1 or nx == r or ny == -1 or ny == c:
            dir = (dir + 1) % 4
            continue

        room[x][y], prev = prev, room[x][y]
        x, y = nx, ny


for _ in range(t):
    fine_dust()
    air_top()
    air_bottom()

result = 2
for i in room:
    result += sum(i)
print(result)
