# 타일 코드
# 수학, 다이나믹 프로그래밍, 조합론
import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 31

dp[0] = 1
dp[1] = 1
dp[2] = 3
# 중복 고려안할 경우
for i in range(3, 31):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

# 대칭되는 경우 제외
# 1. 실제는 다르지만 거울 대칭 시 대칭인 경우
# 2. 원본이 대칭인 경우
if n % 2 == 1:
    print((dp[n] + dp[(n - 1) // 2]) // 2)
else:
    print((dp[n] + dp[n // 2] + dp[(n - 2) // 2] * 2) // 2)
