# 공유기 설치
# 이분 탐색, 매개 변수 탐색
import sys

input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
l = 0
r = arr[-1] - arr[0]
result = 0

# 이진탐색을 통해 공유기 간 거리 찾기
while l <= r:
    mid = (l + r) // 2  # 공유기 설치거리
    cur = arr[0]  # 현재 공유기를 설치할 집
    cnt = 1

    for i in range(1, n):
        # 현재 위치에서 다음 집과의 거리가 mid 이상이면
        if arr[i] >= cur + mid:
            cnt += 1  # 공유기 설치
            cur = arr[i]  # 현 위치 갱신

    if cnt >= c:  # 설치된 개수가 c 이상이면 더 넓게 설치 가능
        l = mid + 1
        result = mid
    else:  # c 미만이면 더 좁게
        r = mid - 1

print(result)
