# 1학년
# 다이나믹 프로그래밍
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
# 특정 인덱스에서 현재까지의 수가 나올 수 있는 경우의 수
# dp[idx번째 수][현재까지의 수] = 가능한 경우
dp = [[0] * 21 for i in range(n)]
dp[0][arr[0]] += 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j]:
            # 다음 숫자를 더하거나 뺐을 때 0~20이면
            # 이전 경우인 dp[i-1][j]를 더함
            if j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[n-2][arr[-1]])
