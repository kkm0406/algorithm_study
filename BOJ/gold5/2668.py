# 숫자고르기
# 그래프 이론, 그래프 탐색, 깊이 우선 탐색
import sys

input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

cnt = 0

# 현재 좌표, 시작한 좌표
def dfs(now, start):
    visited[now] = True
    node = arr[now]
    # 방문안한 좌표먼 계속 탐색
    if not visited[node]:
        dfs(node, start)
    
    # 이미 방문한 좌표 + 시작좌표면
    elif visited[node] and node == start:
        result.append(node)


result = []
for i in range(1, n+1):
    visited = [False] * (n + 1)
    dfs(i, i)

print(len(result))
for i in sorted(result):
    print(i)
