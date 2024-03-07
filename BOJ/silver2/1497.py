# 기타콘서트
# 수학, 브루트포스 알고리즘, 조합론, 비트마스킹, 백트래킹
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
combs = []
nums = 0  # 연주할 곡
result = 1e9  # 그 때 필요한 기타
for _ in range(n):
    a, b = input().split()
    tmp = []
    # 각 기타가 연주할 수 있는 곡 번호
    for i in range(m):
        if b[i] == "Y":
            tmp.append(i)
    arr.append(tmp)

# 개수를 늘려가며 기타 조합 구하기
for i in range(1, n + 1):
    combs += list(combinations([i for i in range(0, n)], i))

# 각 조합에서
for comb in combs:
    # 연주할 수 있는 곡
    song = set()
    for c in comb:
        tmp = arr[c]
        for i in tmp:
            song.add(i)
    # 최대한 많은 곡을 칠 수 있게 if문 사용
    if len(song) > nums:
        result = len(comb)
        nums = len(song)

print(result if nums != 0 else -1)
