# 사과나무
# 브루트포스 알고리즘, 누적 합
import sys

input = sys.stdin.readline

N = int(input())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        arr[i][j] = arr[i][j - 1] + arr[i - 1][j] - arr[i - 1][j - 1] + arr[i][j]

result = arr[1][1]
for k in range(N):
    for i in range(1, N - k + 1):
        for j in range(1, N - k + 1):
            val = arr[i + k][j + k] - arr[i - 1][j + k] - arr[i + k][j - 1] + arr[i - 1][j - 1]
            result = max(result, val)

print(result)