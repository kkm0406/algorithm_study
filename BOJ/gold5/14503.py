# 로봇 청소기
# 구현, 시뮬레이션
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
dir = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
cnt = 0
while True:
    # 청소되지 않은 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2  # 청소 표시
        cnt += 1
    else:
        # 주변 4칸 탐색
        for i in range(4):
            d = (d + 3) % 4  # 반시계 방향 회전
            nx, ny = r + dir[d][0], c + dir[d][1]  # 바라보는 방향 기준 앞쪽 좌표
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
                # 청소 가능한 칸이면 이동
                r, c = nx, ny
                break
        # 주변 4칸 중 청소 가능한 칸이 없는 경우
        else:
            # 현재 방향 유지한 채 한 칸 후진한 좌표
            mx, my = r - dir[d][0], c - dir[d][1]
            # 한 칸 후진할 수 있는 경우
            if room[mx][my] == 0 or room[mx][my] == 2:
                r, c = mx, my
            # 후진 시 벽에 만날 경우
            elif room[mx][my] == 1:
                break

print(cnt)
