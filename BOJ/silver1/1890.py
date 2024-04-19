# 점프
# 다이나믹 프로그래밍
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        move = arr[i][j]
        if move + i < n:
            dp[move + i][j] += dp[i][j]
        if move + j < n:
            dp[i][move + j] += dp[i][j]

print(dp[-1][-1])
