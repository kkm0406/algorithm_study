# 가장 긴 증가하는 부분 수열
# 다이나믹 프로그래밍
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            dp[j] = max(dp[i]+1, dp[j])

print(max(dp))
