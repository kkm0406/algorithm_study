# Lv.3 택배 마스터 광우

import sys
from itertools import permutations

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
perms = list(permutations(arr, n))
ans = []
for perm in perms:
    bucket = 0
    perm_result = 0
    cnt = 0
    idx = 0

    while cnt != k:
        if bucket + perm[idx] <= m:
            bucket += perm[idx]
            idx += 1
            idx %= n
        else:
            perm_result += bucket
            bucket = 0
            cnt += 1

    ans.append(perm_result)

ans.sort()
print(ans[0])
