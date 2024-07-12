# 파이프 옮기기 1
# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색
# dfs 풀이

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0


def dfs(x, y, dir):
    global result
    if x == n - 1 and y == n - 1:
        result += 1
        return

    if dir == 1:
        if y + 1 < n and arr[x][y + 1] == 0:
            dfs(x, y + 1, 1)
        if x + 1 < n and y + 1 < n:
            if arr[x+1][y] == 0 and arr[x + 1][y + 1] == 0 and arr[x][y+1] == 0:
                dfs(x + 1, y + 1, 2)
    if dir == 2:
        if y + 1 < n and arr[x][y + 1] == 0:
            dfs(x, y + 1, 1)
        if x + 1 < n and y + 1 < n:
            if arr[x+1][y] == 0 and arr[x + 1][y + 1] == 0 and arr[x][y+1] == 0:
                dfs(x + 1, y + 1, 2)
        if x + 1 < n and arr[x + 1][y] == 0:
            dfs(x + 1, y, 3)
    if dir == 3:
        if x + 1 < n and y + 1 < n:
            if arr[x+1][y] == 0 and arr[x + 1][y + 1] == 0 and arr[x][y+1] == 0:
                dfs(x + 1, y + 1, 2)
        if x + 1 < n and arr[x + 1][y] == 0:
            dfs(x + 1, y, 3)


dfs(0, 1, 1)

print(result)
