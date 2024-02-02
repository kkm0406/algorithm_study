# Lv.2 연탄의 크기
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = 0
# 난로 크기가 연탄 크기의 배수일 때 사용가능
for i in range(2, max(arr)+1):
    r = i # 연탄
    cnt = 0
    for a in arr: # 난로 크기
        if r > a:
            continue
        if a % r == 0:
            cnt += 1
    result = max(cnt, result)

print(result)

