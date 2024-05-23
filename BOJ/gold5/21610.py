# 마법사 상어와 비바라기
# 구현, 시뮬레이션
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dir_x = [-1, -1, 1, 1]
dir_y = [-1, 1, -1, 1]
clouds = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

for _ in range(m):
    d, s = map(int, input().split())
    d = d - 1

    for i in range(len(clouds)):
        clouds[i][0] = (clouds[i][0] + dx[d]*s) % n
        clouds[i][1] = (clouds[i][1] + dy[d]*s) % n

    for cx, cy in clouds:
        board[cx][cy] += 1

    # 물복사
    water_copy = []
    for cx, cy in clouds:
        cnt = 0
        for i in range(4):
            nx = cx + dir_x[i]
            ny = cy + dir_y[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                cnt += 1
        board[cx][cy] += cnt

    for cx, cy, cnt in water_copy:
        board[cx][cy] += cnt

    visited = [[False]*n for _ in range(n)]
    for cx, cy in clouds:
        visited[cx][cy] = True

    new_cloud = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and not visited[i][j]:
                board[i][j] -= 2
                new_cloud.append([i, j])

    clouds.clear()
    clouds = new_cloud

total = 0
for i in board:
    total += sum(i)

print(total)

