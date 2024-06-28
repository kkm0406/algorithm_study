# Lv.3 나무 조경

import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

if n == 2:
    max_depth = 2
else:
    max_depth = 4

visited = [[False] * n for _ in range(n)]

result = 0


def dfs(depth, pick):
    global result
    if depth == max_depth:
        result = max(result, sum(pick))
    else:
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    visited[i][j] = True
                    pick.append(arr[i][j])
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                pick.append(arr[nx][ny])
                                dfs(depth + 1, pick)
                                pick.pop()
                                visited[nx][ny] = False
                    pick.pop()
                    visited[i][j] = False


dfs(0, [])
print(result)
