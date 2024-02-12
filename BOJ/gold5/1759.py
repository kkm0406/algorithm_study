# 암호 만들기

import sys
from itertools import combinations

input = sys.stdin.readline

l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()
combs = list(combinations(alpha, l))
vowels = set(['a', 'e', 'i', 'o', 'u'])
result = []
for comb in combs:
    v, c = 0, 0
    for w in comb:
        if w in vowels:
            v += 1
        else:
            c += 1
    if c >= 2 and v >= 1:
        result.append(comb)

for i in sorted(result):
    print("".join(i))
