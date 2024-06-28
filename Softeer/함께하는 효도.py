import sys
from itertools import permutations
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
pos = []
for _ in range(m):
    x, y = map(int, input().split())
    pos.append((x-1, y-1))

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def dfs(x, y, score, d, path):
    global mx_score, mx_path
    visited[x][y] = True
    score += grid[x][y]
    path.append((x, y))
    if d == 3:
        if mx_score < score:
            mx_score = score
            mx_path = path[:]
        return
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and not (nx, ny) in total_path:
            dfs(nx, ny, score, d+1, path)
            visited[nx][ny] = False
            path.pop()
perm = list(permutations(pos, m))
ans = 0
for perm_case in perm:
    total_path = []
    total_score = 0
    for x, y in perm_case:
        mx_score, mx_path = 0, []
        dfs(x, y, 0, 0, [])
        total_path += mx_path
        total_score += mx_score
    ans = max(ans, total_score)
print(ans)