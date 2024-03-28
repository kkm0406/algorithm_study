# 행렬
# 그리디 알고리즘
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
b = [list(map(int, list(input().strip()))) for _ in range(n)]
cnt = 0


# 3x3 행렬 변환 함수
def convert(i, j, a):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            a[x][y] = 1 - a[x][y]


# 행렬 탐색
for i in range(n - 2):
    for j in range(m - 2):
        # 변환할 행렬의 원소가 b 행렬과 불일치시 행렬 변환
        if a[i][j] != b[i][j]:
            cnt += 1
            convert(i, j, a)

if a != b:
    print(-1)
else:
    print(cnt)
