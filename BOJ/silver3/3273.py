# 두 수의 합
# 정렬, 투 포인터

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
# 투포인터를 위해 정렬
arr.sort()

# 양 끝에서부터
l, r = 0, n - 1
cnt = 0
while l < r:
    result = arr[l] + arr[r]
    # 합이 x보다 작으면 더 키워야 함
    # -> l 이동
    if result < x:
        l += 1
    # 아닐땐 값 줄여야함
    # -> r 이동
    else:
        if result == x:
            cnt += 1
        r -= 1
print(cnt)
