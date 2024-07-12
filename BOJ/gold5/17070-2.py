# 파이프 옮기기 1
# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색
# dp 풀이

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 0: 가로, 1: 세로, 2: 대각선
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

# (0,1)에는 가로방향 파이프
dp[0][1][0] = 1
# 0행 가로 방향
for i in range(2, n):
    if arr[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(1, n):
    for j in range(1, n):
        # 파이프 놓을 수 있으면
        if arr[i][j] == 0:
            # 이전 열의 가로방향 + 대각선 방향
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
            # 이전 행의 세로방향 + 대각선
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]

            # 대각선 방향으로 놓을 수 있는 경우
            if arr[i - 1][j] == 0 and arr[i][j - 1] == 0:
                # (i-1, j-1)의 가로, 세로, 대각선 방향의 경우의 수
                dp[i][j][2] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

print(sum(dp[-1][-1]))