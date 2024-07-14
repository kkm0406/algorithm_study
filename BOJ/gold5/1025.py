# 제곱수 찾기
# 브루트포스 알고리즘
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

result = -1


def is_sqrt(num):
    if int(num ** 0.5) ** 2 == num:
        return True
    else:
        return False


for i in range(n):  # 시작 x좌표
    for j in range(m):  # 시작 y좌표
        for row_d in range(-n, n):  # 행의 등차
            for col_d in range(-m, m):  # 열의 등차
                num = ""  # 선택한 숫자
                x, y = i, j  # x, y가 등차에 따라 이동하며 숫자를 선택

                if row_d == 0 and col_d == 0:
                    continue

                while 0 <= x < n and 0 <= y < m:
                    num += str(arr[x][y])
                    if is_sqrt(int(num)):  # 완전제곱수이면
                        result = max(result, int(num))
                    x += row_d
                    y += col_d

print(result)
