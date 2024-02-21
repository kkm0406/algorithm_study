# 내려가기
# 다이나믹 프로그래밍, 슬라이딩 윈도우
import sys

input = sys.stdin.readline
n = int(input())
# 메모리 제한으로 2x3 배열 선언
min_dp = [[0] * 3 for _ in range(2)]
max_dp = [[0] * 3 for _ in range(2)]

for i in range(n):
    arr = list(map(int, input().split()))

    max_dp[1][0] = max(max_dp[0][0], max_dp[0][1]) + arr[0]
    max_dp[1][1] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + arr[1]
    max_dp[1][2] = max(max_dp[0][1], max_dp[0][2]) + arr[2]

    min_dp[1][0] = min(min_dp[0][0], min_dp[0][1]) + arr[0]
    min_dp[1][1] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + arr[1]
    min_dp[1][2] = min(min_dp[0][1], min_dp[0][2]) + arr[2]

    # 2x3 배열을 계속 갱신
    # i번째 배열에 영향을 주는 것은 i-1번째 배열
    max_dp[0][0], max_dp[0][1], max_dp[0][2] = max_dp[1][0], max_dp[1][1], max_dp[1][2]
    min_dp[0][0], min_dp[0][1], min_dp[0][2] = min_dp[1][0], min_dp[1][1], min_dp[1][2]

print(max(max_dp[-1]), min(min_dp[-1]))