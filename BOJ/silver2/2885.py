# 초콜릿 식사
# 수학, 그리디 알고리즘, 정수론
import sys

input = sys.stdin.readline
k = int(input())
size = 1
# k보다 크면서 가장 작은 2^n
while True:
    if size >= k:
        break
    size *= 2

print(size, end=" ")
cnt = 0
# size를 반씩 줄이면서 k에서 해당 size만큼 제거
# ex) size = 8, k = 6
# 1. size = 4, k = 2
# 2. size = 2, k = 0
while True:
    if k <= 0:
        break
    if k >= size:
        k -= size
    else:
        size //= 2
        cnt += 1

print(cnt)
