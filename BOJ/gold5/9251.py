# LCS
# 다이나믹 프로그래밍, 문자열
import sys

input = sys.stdin.readline

s = [""]+list(input().strip())
t = [""]+list(input().strip())
dp = [[0] * (len(s)) for _ in range(len(t))]
result = 0
for i in range(1, len(t)):
    for j in range(1, len(s)):
        if t[i] == s[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # 알파벳이 다른 경우 이전까지 비교한 값중 최대값
            # CAP와 ACA를 비교할 때 마지막 P와 A는 서로 다름
            # 따라서 CAP와 AC의 LCS = 1
            # CA와 ACA의 LCS = 2 중 최대값
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(dp[-1]))