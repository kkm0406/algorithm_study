# 합분해
# 수학, 다이나믹 프로그래밍
import sys

input = sys.stdin.readline
n, k = map(int, input().split())

# dp[k][n]: n을 k개 숫자 조합으로 만드는 방법
dp = [[0] * (n+1) for i in range(k+1)]

# k=1인 방법은 모두 1
for i in range(1, n+1):
    dp[1][i] = 1

# n이 1인 경우는
# k:1 -> 1, k:2 -> 1+0, 0+1, k:3 -> 300 030 003
for i in range(1, k+1):
    dp[i][1] = i

# 표 그려서 점화식 찾기
for i in range(2, k+1):
    for j in range(2, n+1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000


print(dp[k][n])
