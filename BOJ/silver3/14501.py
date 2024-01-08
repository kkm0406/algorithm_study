# 퇴사
# 다이나믹 프로그래밍, 브루트포스 알고리즘

import sys

input = sys.stdin.readline
n = int(input())
t, p = [], []
dp = [0 for i in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n - 1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담 x
    if i + t[i] > n:
        dp[i] = dp[i + 1]
    # i일에 상담을 안할 때와 할 때 비교
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])

print(max(dp))
