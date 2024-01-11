# 설탕 배달
# 수학, 다이나믹 프로그래밍, 그리디 알고리즘

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 5001
# 3과 5일 때 필요한 설탕봉투 개수
dp[3], dp[5] = 1, 1

for i in range(6, 5001):
    # 5kg 하나만 추가하면 되는 경우
    if dp[i - 3] == 0 and dp[i - 5] != 0:
        dp[i] = dp[i - 5] + 1
    # 3kg 하나만 추가하면 되는 경우
    elif dp[i - 3] != 0 and dp[i - 5] == 0:
        dp[i] = dp[i - 3] + 1
    # 3kg, 5kg 둘다 가능한 경우면 최솟값 비교
    # ex) 8 = 기존 3kg에서 5kg 추가 or 기존 5kg에서 3kg 추가
    elif dp[i - 3] != 0 and dp[i - 5] != 0:
        dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)

print(dp[n] if dp[n] != 0 else -1)
