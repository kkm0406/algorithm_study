# 수리공 항승
# 그리디 알고리즘, 정렬
import sys

input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
# 처음 테이프를 붙이는 지점
idx = arr[0] + l - 0.5
cnt = 1
while arr:
    # 물이 새는 첫번째 위치가 테이프의 범위 안이면
    if arr[0] <= idx:
        # 해당 위치 수리
        arr.pop(0)
    # 못막는 범위이면
    else:
        # 새로운 테이프 추가
        idx = arr[0] + l - 0.5
        cnt += 1
        # 해당 위치 수리
        arr.pop(0)

print(cnt)
