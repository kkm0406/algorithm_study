# 쉬운 계단 수
# 다이나믹 프로그래밍
import sys

input = sys.stdin.readline
n = int(input())
# 각 숫가자 앞에 올 때의 계단 수
dp = [[0] * 10 for i in range(n + 1)]
# 한자리 수에서 계단 수
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n + 1):
    for j in range(10):
        # 0이 맨 앞에 오는 경우는 한가지
        # n == 1 -> 0, n == 2 -> 01 n == 3 -> 010, 012
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            # ex) 1 ~ 8은 뒤에 올 숫자가 2종류
            # 2자리에서 -> 21, 23
            # 앞에 오는 숫자 -1 경우 + 앞에 오는 숫자 + 1 경우
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)
