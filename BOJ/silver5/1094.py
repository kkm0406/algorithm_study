# 막대기
# 수학, 비트마스킹
import sys

input = sys.stdin.readline
x = int(input())
stick = 64
cnt = 1
while x > 0:
    if stick > x:
        stick = stick // 2
    else:
        cnt += 1
        x -= stick

print(cnt)
