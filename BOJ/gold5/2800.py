# 괄호 제거
# 자료 구조, 문자열, 브루트포스 알고리즘, 비트마스킹, 스택
import sys
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline

s = list(input().strip())
st = []  # 괄호 쌍 인덱스
tmp = []  # 괄호 찾기용 스택
result = []
for i in range(len(s)):
    if s[i] == "(":
        tmp.append(i)
    elif s[i] == ")":
        tmp_idx = tmp.pop()
        # 괄호 쌍의 인덱스 저장
        st.append([tmp_idx, i])

combs = []

# 제거할 괄호 조합 생성
for i in range(1, len(st) + 1):
    combs += list(combinations(st, i))

for comb in combs:
    string = deepcopy(s)
    # 해당 위치의 괄호 제거
    for c in comb:
        string[c[0]] = ""
        string[c[1]] = ""
    result.append("".join(string))

result = list(set(result))
for i in sorted(result):
    print(i)