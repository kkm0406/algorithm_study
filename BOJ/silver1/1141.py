# 접두사
# 그리디 알고리즘, 문자열, 정렬

import sys

input = sys.stdin.readline
n = int(input())
arr = [input().strip() for _ in range(n)]
# 접두사를 찾기 위해 길이 순 정렬
arr = sorted(arr, key=lambda x: (len(x)))
cnt = 0
for i in range(n):
    # 현재 단어보다 긴 단어에서 탐색
    for j in range(i + 1, n):
        # 현대 단어를 접두사로 쓰는 단어가 있으면 break
        if arr[i] == arr[j][:len(arr[i])]:
            break
    else:
        cnt += 1

print(cnt)
