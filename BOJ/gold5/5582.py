# 공통 부분 문자열
# 다이나믹 프로그래밍, 문자열
import sys

input = sys.stdin.readline

s = input().strip()
t = input().strip()
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
result = 0
for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        # 문자가 같으면
        if s[i - 1] == t[j - 1]:
            # 그전까지 공통 부분 문자열 길이 + 1
            dp[i][j] = dp[i - 1][j - 1] + 1
            result = max(result, dp[i][j])

print(result)
