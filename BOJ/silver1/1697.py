# 숨바꼭질
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 100001

q = deque()
q.append(n)

while q:
    now = q.popleft()
    if now == k:
        print(visited[k])
        break

    for dx in (now - 1, now + 1, now * 2):
        if 0 <= dx <= 100000 and visited[dx] == 0:
            visited[dx] = visited[now] + 1
            q.append(dx)
