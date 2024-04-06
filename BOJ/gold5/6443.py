# 애너그램
# 문자열, 백트래킹
import sys
from collections import deque, Counter, defaultdict

input = sys.stdin.readline


def dfs(depth, result):
    if depth == len(s):
        print("".join(result))
        return
    for i in s:
        if cnt[i]:
            cnt[i] -= 1
            result.append(i)
            dfs(depth + 1, result)
            result.pop()
            cnt[i] += 1


for _ in range(int(input())):
    s = input().strip()
    # 사전순 정렬 -> 백트래킹 결과도 사전순으로 나옴
    s = sorted(list(s))
    # s의 알파벳 개수를 정렬
    cnt = defaultdict(int)
    for i in s:
        cnt[i] += 1
    result = []

    dfs(0, result)
