# 프린터큐
# 구현, 자료 구조, 시뮬레이션, 큐

import sys
from collections import deque
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        q.append([arr[i], i])
    cnt = 0
    while q:
        max_num = max(q)[0]
        front, idx = q[0]  # 맨 앞의 중요도 확인
        if front == max_num:  # 가장 중요도 높은 문서
            q.popleft()  # 인쇄
            cnt += 1
            if idx == m:  # 인쇄할 문서와 동일한 문서일 때
                print(cnt)
                break
        else:
            # 큐의 가장 뒤에 재배치
            tmp, tmp_idx = q.popleft()
            q.append([tmp, tmp_idx])

