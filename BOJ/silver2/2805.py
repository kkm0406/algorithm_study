# 나무 자르기
# 이분 탐색, 매개 변수 탐색
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
heights = list(map(int, input().split()))

#0부터 시작
l, r = 0, max(heights)
result = 0
while l <= r:
    cut = 0
    mid = (l + r) // 2
    for h in heights:
        if h > mid:
            cut += (h - mid)

    # 가져가는 나무의 길이가 필요한만큼 보다 적으면
    if cut < m:
        r = mid - 1
    # 필요한거보다 더 가져가는 경우
    else:
        l = mid + 1
        result = mid

print(result)
