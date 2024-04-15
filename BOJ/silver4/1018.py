# 체스판 다시 칠하기
# 브루트포스 알고리즘
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
result = n * m


def chess(i, j):
    global result
    b_start = 0
    w_start = 0
    # (0, 0)이 b로 시작하는 경우
    for r in range(i, i + 8):
        for c in range(j, j + 8):
            if (r + c) % 2 == 0:  # 짝수 인덱스에 b가 있어야 함
                if board[r][c] == "W":
                    b_start += 1
            else:
                if board[r][c] == "B":
                    b_start += 1
    # (0, 0)이 w로 시작하는 경우
    for r in range(i, i + 8):
        for c in range(j, j + 8):
            if (r + c) % 2 == 0:  # 짝수 인덱스에 w가 있어야 함
                if board[r][c] == "B":
                    w_start += 1
            else:
                if board[r][c] == "W":
                    w_start += 1

    result = min(result, min(b_start, w_start))


for i in range(n - 7):
    for j in range(m - 7):
        chess(i, j)

print(result)
