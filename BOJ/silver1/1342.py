# 행운의 문자열

import sys
from collections import Counter

input = sys.stdin.readline

s = input().strip()
n = len(s)
cnt = 0
# 알파벳 별 개수
alpha = Counter(s)


# 이전 단어, depth
def dfs(prev, depth):
    global cnt
    # 단어 길이 만큼 재귀 -> 인접한 모든 문자가 같이 않은 경우
    if depth == n:
        cnt += 1

    # 알바펫 순회하며 재배치
    for w in alpha.keys():
        # 이전 문자와 같거나, 더 이상 배치할 문자가 없는 경우 continue
        if w == prev or alpha[w] == 0:
            continue
        # 문자 사용
        alpha[w] -= 1
        # 재귀
        dfs(w, depth + 1)
        # 원상태 복귀
        alpha[w] += 1


dfs("", 0)
print(cnt)
