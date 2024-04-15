# 배열 복원하기
# 구현
from sys import stdin

input = stdin.readline

h, w, x, y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h + x)]
a = []
b = []
for i in range(x, h + x):
    b.append(arr[i][y:y + w])
for i in range(h):
    a.append(arr[i][:w])


for i in range(x, h):
    for j in range(y, w):
        a[i][j] -= a[i-x][j-y]

for i in a:
    print(*i)