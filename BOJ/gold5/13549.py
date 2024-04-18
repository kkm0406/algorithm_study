# 숨바꼭질 3
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 데이크스트라, 최단 경로, 0-1 너비 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
visited = [-1] * 100001
q = deque()
q.append(n)
visited[n] = 0

while q:
    now = q.popleft()
    if now == k:
        print(visited[k])
        break

    # 4, 6 (4->3->6)의 경우 -> -1, 1, *2순으로 탐색
    for next in (now - 1, now + 1, now * 2):
        if 0 <= next <= 100000 and visited[next] == -1:
            if next == now * 2:
                visited[next] = visited[now]
                q.appendleft(next) # 이동의 가중치가 다르므로 appendleft
            else:
                visited[next] = visited[now] + 1
                q.append(next)
