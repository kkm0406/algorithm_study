# Lv.3 성적 평균

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [0]
for i in range(1, n + 1):
    dp.append(dp[-1] + arr[i])

for _ in range(k):
    a, b = map(int, input().split())
    total = dp[b] - dp[a - 1]
    size = b - a + 1
    print("%0.2f" % float(total / size))
