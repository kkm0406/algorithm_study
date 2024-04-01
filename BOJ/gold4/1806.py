# 부분합
# 누적 합, 투 포인터
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
size = sys.maxsize
l, r = 0, 0
result = arr[l]
if arr[l] == s:
    print(1)
    exit()

while r < n:
    if result >= s:
        size = min(size, r - l + 1)
        result -= arr[l]
        l += 1
    else:
        r += 1
        if r < n:
            result += arr[r]
        else:
            break

if size == sys.maxsize:
    print(0)
else:
    print(size)
