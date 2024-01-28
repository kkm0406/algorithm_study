# 약속
# 수학, 정렬
import sys

input = sys.stdin.readline

n = int(input())
time = []
for i in range(n):
    a, b = map(int, input().split())
    time.append(b - a)

time.sort()

if len(time) % 2 == 1:
    print(1)
else:
    print(time[n // 2] - time[n // 2 - 1] + 1)
