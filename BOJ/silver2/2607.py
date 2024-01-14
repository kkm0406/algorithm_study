# 비슷한 단어
# 구현, 문자열

import sys
from collections import Counter
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
target = input().strip()
arr = [input().strip() for _ in range(n - 1)]
answer = 0
for word in arr:
    # 첫 번째 단어를 리스트화
    tmp_target = list(target)
    cnt = 0
    for w in word:
        # 타겟 단어에 속한 문자이면
        if w in tmp_target:
            # 타겟 단어에서 제거
            tmp_target.remove(w)
        # 타겟 단어에 속하지 않은 문자 수
        else:
            cnt += 1
    # 연산 후 타켓 단어의 길이가 1이하고
    # 타겟 단어에 속하지 않은 문자가 1개 이하
    if len(tmp_target) <= 1 and cnt <= 1:
        answer += 1

print(answer)
