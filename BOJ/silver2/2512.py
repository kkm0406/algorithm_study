# 예산
# 이분 탐색, 매개 변수 탐색
from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
l, r = 1, max(arr)
result = 0
while l <= r:
    mid = (l + r) // 2
    sum = 0
    for i in arr:
        if i < mid:
            sum += i
        else:
            sum += mid

    if sum > m:
        r = mid-1
    else:
        l = mid +1
        result = mid

print(result)