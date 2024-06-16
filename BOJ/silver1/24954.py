# 물약 구매
# 구현, 브루트포스 알고리즘, 백트래킹
import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
cost = list(map(int,input().split()))
sale = [[] for _ in range(n)]
for i in range(n):
    m=int(input())
    for _ in range(m):
        sale[i].append(list(map(int,input().split())))

perms = list(permutations(range(0, n), n))
result = sys.maxsize

for perm in perms:
    tmp_cost = cost[:]
    price = 0

    for item in perm:
        price += tmp_cost[item]
        for a, d in sale[item]:
            tmp_cost[a-1] = max(1, tmp_cost[a-1]-d)

    result = min(price, result)

print(result)
