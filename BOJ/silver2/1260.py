# DFS와 BFS
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

from sys import stdin
from collections import deque

input = stdin.readline
n, m, v = map(int, input().split())
arr = [[] for i in range(n + 1)]
visited_d = [False] * (n + 1)
visited_b = [False] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 방문 정점이 여러 개인 경우 작은 번호부터 방문
for i in arr:
    i.sort()


def dfs(node):
    visited_d[node] = True
    print(node, end=" ")
    for next in arr[node]:
        if not visited_d[next]:
            dfs(next)


dfs(v)
print()


def bfs(start):
    q = deque()
    q.append(start)
    visited_b[start] = True

    while q:
        now = q.popleft()
        print(now, end=" ")
        for next in arr[now]:
            if not visited_b[next]:
                visited_b[next] = True
                q.append(next)


bfs(v)
