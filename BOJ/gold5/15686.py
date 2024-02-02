# 치킨 배달

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 0빈칸, 1집, 2치킨
home, chicken = [], []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])
result = sys.maxsize
pick = []


def dfs(depth, idx):
    global result

    if depth == m:
        dist = 0
        for hx, hy in home:
            cost = 1e9
            for px, py in pick:
                cost = min(cost, abs(hx - px) + abs(hy - py))
            dist += cost
        result = min(result, dist)
    else:
        for i in range(idx, len(chicken)):
            pick.append(chicken[i])
            dfs(depth + 1, idx + 1)
            pick.pop()


for i in range(len(chicken)):
    dfs(0, i)

print(result)
