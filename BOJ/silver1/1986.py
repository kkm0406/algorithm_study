# 체스
# 구현
import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n, m = map(int, input().split())
board = [["O"] * m for _ in range(n)]
arr = list(map(int, input().split()))
queen, knight, pawn = [], [], []
size = arr[0] * 2
for i in range(1, size + 1, 2):
    queen.append([arr[i] - 1, arr[i + 1] - 1])
    board[arr[i] - 1][arr[i + 1] - 1] = 'Q'
arr = list(map(int, input().split()))
size = arr[0] * 2
for i in range(1, size + 1, 2):
    knight.append([arr[i] - 1, arr[i + 1] - 1])
    board[arr[i] - 1][arr[i + 1] - 1] = 'K'
arr = list(map(int, input().split()))
size = arr[0] * 2
for i in range(1, size + 1, 2):
    pawn.append([arr[i] - 1, arr[i + 1] - 1])
    board[arr[i] - 1][arr[i + 1] - 1] = 'P'


# 재귀로 퀸의 이동 경로 탐색
def move_queen(x, y, d):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if board[x][y] != "P" and board[x][y] != "K" and board[x][y] != "Q":
        board[x][y] = "X"

        if d == 0:
            move_queen(x + 1, y, 0)
        elif d == 1:
            move_queen(x - 1, y, 1)
        elif d == 2:
            move_queen(x, y + 1, 2)
        elif d == 3:
            move_queen(x, y - 1, 3)
        elif d == 4:
            move_queen(x + 1, y + 1, 4)
        elif d == 5:
            move_queen(x + 1, y - 1, 5)
        elif d == 6:
            move_queen(x - 1, y + 1, 6)
        elif d == 7:
            move_queen(x - 1, y - 1, 7)
        return True
    return False


# 재귀로 나이트의 이동 경로 탐색
def move_knight(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if board[x][y] != "P" and board[x][y] != "K" and board[x][y] != "Q":
        board[x][y] = "X"
        return True
    return False


def check_queen():
    for i in range(len(queen)):
        x, y = queen[i]
        move_queen(x + 1, y, 0)
        move_queen(x - 1, y, 1)
        move_queen(x, y + 1, 2)
        move_queen(x, y - 1, 3)
        move_queen(x + 1, y + 1, 4)
        move_queen(x + 1, y - 1, 5)
        move_queen(x - 1, y + 1, 6)
        move_queen(x - 1, y - 1, 7)


def check_night():
    for i in range(len(knight)):
        x, y = knight[i]
        move_knight(x + 2, y + 1)
        move_knight(x + 2, y - 1)
        move_knight(x - 2, y + 1)
        move_knight(x - 2, y - 1)
        move_knight(x + 1, y - 2)
        move_knight(x - 1, y - 2)
        move_knight(x + 1, y + 2)
        move_knight(x - 1, y + 2)


check_queen()
check_night()

result = 0
for i in board:
    result += i.count("O")
print(result)
