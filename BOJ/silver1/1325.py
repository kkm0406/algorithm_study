# 효율적인 해킹
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
computer = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    computer[b].append(a)

cnt = [0] * (n + 1)


def bfs(i):
    visited = [False] * (n + 1)
    visited[i] = True
    q = deque()
    q.append(i)
    cnt = 1
    while q:
        x = q.popleft()

        for next in computer[x]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                q.append(next)
    return cnt


for i in range(1, n + 1):
    cnt[i] = bfs(i)

result = max(cnt)

for i in range(1, n + 1):
    if cnt[i] == result:
        print(i, end=" ")
