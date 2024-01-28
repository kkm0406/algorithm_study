# RGB거리
# 다이나믹 프로그래밍
import sys

input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]  # rgb에 따라 해당 집을 칠하는 비용
dp[0] = rgb[0]

for i in range(1, n):
    # i번째를 r로 칠할때: i번째 집을 r로 칠하는 비용 + i-1번째 집을 칠하는 최소 비용
    dp[i][0] = rgb[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    # i번째를 g로 칠할때: i번째 집을 g로 칠하는 비용 + i-1번째 집을 칠하는 최소 비용
    dp[i][1] = rgb[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    # i번째를 b로 칠할때: i번째 집을 b로 칠하는 비용 + i-1번째 집을 칠하는 최소 비용
    dp[i][2] = rgb[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[-1]))
