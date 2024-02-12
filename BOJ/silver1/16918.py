# 봄버맨

import sys
from collections import deque

input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 1초가 지남 -> 처음 상태
# 2초, 4초, 6초, ... -> 모든 칸이 폭탄
# 3초 -> 처음 폭탄이 터짐
# 5초 -> 처음 폭탄이 터지는 범위 밖의 폭탄이 터짐
# 7초 -> 폭탄이 터짐
# 9초 -> 폭탄이 터지는 범위 밖의 폭탄이 터짐

# 모든 폭탄이 터짐
def explode():
    while q:
        x, y = q.popleft()
        board[x][y] = "."
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'O':
                board[nx][ny] = '.'


def bomb(time):
    global q, board
    if time == 1:
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    q.append((i, j))
    elif time % 2 == 1:
        # 3초가 지난 폭탄을 폭발
        explode()
        # 3초 후에 터질 폭탄을 저장
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    q.append((i, j))
    else:
        # 모든 칸에 폭탄 설치
        for i in range(r):
            for j in range(c):
                board[i][j] = "O"


for i in range(1, n + 1):
    bomb(i)

for i in board:
    print("".join(i))
