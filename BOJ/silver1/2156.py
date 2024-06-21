# 포도주 시식
# 다이나믹 프로그래밍
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# 포도주 먹는 경우
# 1. 현재 포도주를 먹지 않는 경우
# 2. i번째 포도주, i-1번째 포도주는 먹고 i-2번째 포도주는 스킵
# 3. i번째 포도주, i-2번째 포도주는 먹고 i-1번째 포도주는 스킵
dp = [0] * n
dp[0] = arr[0]
if n > 1:
    dp[1] = arr[0] + arr[1]
if n > 2:
    dp[2] = max(arr[2] + arr[1], arr[2] + arr[0], dp[1])
for i in range(3, n):
    # dp[i-1]: 현재 포도주 스킵
    # arr[i]+arr[i-1]+dp[i-3]: 번째 포도주, i-1번째 포도주는 먹고 i-2번째 포도주는 스킵
    # arr[i]+dp[i-2]: i번째 포도주, i-2번째 포도주는 먹고 i-1번째 포도주는 스킵
    dp[i] = max(dp[i - 1], arr[i] + arr[i - 1] + dp[i - 3], arr[i] + dp[i - 2])

print(dp[n - 1])
