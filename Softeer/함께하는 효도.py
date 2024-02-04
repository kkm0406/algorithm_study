# LV.3 힘께하는 효도

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
visited = [[False] * n for _ in range(n)]
coords = [[[0, 0] for _ in range(4)] for i in range(m)]
cost = [0] * m


def dfs(idx, depth, prev):
    if depth == 4:
        result = 0
        for px, py in prev:
            result += arr[px][py]
        if result > cost[idx]:
            cost[idx] = result
            for i in range(4):
                coords[idx][i] = prev[i]
    else:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = prev[-1][0] + dx, prev[-1][1] + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(idx, depth + 1, prev + [[nx, ny]])
                visited[nx][ny] = False


for i in range(m):
    x, y = map(int, input().split())
    visited[x - 1][y - 1] = True
    dfs(i, 1, [[x - 1, y - 1]])
    visited[x - 1][y - 1] = False
    for a, b in coords[i]:
        arr[a][b] = 0

    answer += cost[i]

print(answer)
