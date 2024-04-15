# 랜선 자르기
# 이분 탐색, 매개 변수 탐색
import sys

input = sys.stdin.readline
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
l, r = 1, max(arr)
result = 0
while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid

    if cnt >= n:
        l = mid + 1
        result = mid
    else:
        r = mid - 1

print(result)
