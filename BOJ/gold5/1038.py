# 감소하는 수

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(1, 11):
    combs = list(combinations(range(10), i))
    for comb in combs:
        comb = list(comb)
        comb.sort(reverse=True)
        arr.append(int("".join(str(x) for x in comb)))

arr.sort()

print(-1 if len(arr) <= n else arr[n])