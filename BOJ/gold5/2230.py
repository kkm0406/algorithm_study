# 수 고르기
# 정렬, 두 포인터
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

l, r = 0, 1
result = sys.maxsize
while l < n and r < n:
    diff = arr[r] - arr[l]

    if diff < m:
        r += 1
    else:
        l += 1
        result = min(result, diff)

print(result)
