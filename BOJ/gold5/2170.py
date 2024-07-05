# 선 긋기
# 정렬, 스위핑
import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()

px, py = arr[0]
result = py - px
for i in range(1, n):
    nx, ny = arr[i]
    if py >= nx:  # 겹쳐지는 경우
        if ny <= py:  # 아예 기존 선분에 합쳐지는 경우
            continue
        result += abs(ny - py)  # 새로운 범위 추가
        px, py = nx, ny
    else:
        result += (ny - nx)
        px, py = nx, ny

print(result)
