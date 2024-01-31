# 행운의 문자열
# 수학, 브루트포스 알고리즘, 백트래킹
import sys
from collections import Counter

input = sys.stdin.readline

s = input().strip()
n = len(s)

# 알파벳 별 개수
alpha = Counter(s)

# 이전 단어, depth
def dfs(prev, depth):
    answer = 0

    # 단어 길이와 같은 경우
    # 인접한 모든 문자가 같지 않은 경우
    if depth == n:
        return 1

    for w in alpha.keys():
        # 이전 문자와 같거나 해당 문자을 다 쓴 경우
        if w == prev or alpha[w] == 0:
            continue

        alpha[w] -= 1
        answer += dfs(w, depth + 1)
        alpha[w] += 1

    return answer


print(dfs("", 0))
