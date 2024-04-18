# 뱀과 사다리 게임
# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque

n, m = map(int, input().split())

ladders = {}
snake = {}

for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

cnt = [0]*101
q = deque([1])
visited = [False]*101
visited[1] = True
while q:
    x = q.popleft()
    if x==100:
        print(cnt[x])
        break

    for i in range(1, 7):
        next = x+i
        if next<=100:
            if next in ladders.keys():
                next = ladders[next]
            elif next in snake.keys():
                next = snake[next]
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt[next] = cnt[x]+1
