# 동전 1
# 다이나믹 프로그래밍
# 가치의 합이 i원이 되는 경우의 수를 구하는 문제로 세분화
# ex) 1, 2, 5원으로 10원을 만드는 경우
# 1. 1원만 사용하는 경우
# -> dp[1], dp[2], ..., dp[10] = 1
# 2. 1원, 2원을 사용하는 경우
# -> 2-1. 2원 미포함 = 1원만 사용하는 경우
# -> 2-2. 2원 포함 => dp[k-2]를 ㄷ 더함
# val원을 추가할 때 -> dp[k] = dp[k] + dp[k-val]
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
dp = [0] * (k + 1)  # dp[i]: i원을 만드는 경우의 수
dp[0] = 1

for val in arr:
    for j in range(val, k + 1):
        dp[j] = dp[j] + dp[j - val]

print(dp[k])
