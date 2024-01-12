# 지구 온난화
# 구현, 시뮬레이션

import sys

input = sys.stdin.readline

r, c = map(int, input().split())
# 지도에 없거나 범위를 벗어나는 칸도 모두 바다이기 때문에 지도 확장
board = [['.'] + list(input().strip()) + ['.'] for _ in range(r)]
board = [['.'] * (c + 2)] + board + [['.'] * (c + 2)]
island = []  # 잠기는 땅의 좌표


# 인접한 칸에 바다 개수 세기
def check(i, j):
    cnt = 0
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx = i + dx
        ny = j + dy
        if 0 <= nx <= len(board) and 0 <= ny <= len(board[0]) and board[nx][ny] == '.':
            cnt += 1
    return cnt


for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 'X' and check(i, j) >= 3:
            island.append([i, j])

# 50년 이후 바다에 잠기는 땅
for i, j in island:
    board[i][j] = '.'

# 상하좌우 방향에서 이동하면서 지도 크기 축소
n, s, e, w = 0, 0, 0, 0
flags = [True] * 4
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 'X':
            n = i
            flags[0] = False
            break
    if not flags[0]:
        break
for i in range(len(board) - 1, -1, -1):
    for j in range(len(board[0])):
        if board[i][j] == 'X':
            s = i
            flags[1] = False
            break
    if not flags[1]:
        break
for i in range(len(board[0])):
    for j in range(len(board)):
        if board[j][i] == 'X':
            w = i
            flags[2] = False
            break
    if not flags[2]:
        break
for i in range(len(board[0]) - 1, -1, -1):
    for j in range(len(board)):
        if board[j][i] == 'X':
            e = i
            flags[3] = False
            break
    if not flags[3]:
        break

for i in range(n, s + 1):
    print("".join(board[i][w:e + 1]))
