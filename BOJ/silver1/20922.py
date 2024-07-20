# 겹치는 건 싫어
# 두 포인터
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * 100001
l, r = 0, 0
nums = [arr[l], arr[r]]
result = -1

while r < n:
    if cnt[arr[r]] < k:
        cnt[arr[r]] += 1
        r += 1
    else:
        cnt[arr[l]] -= 1
        l += 1

    result = max(result, r - l)

print(result)
