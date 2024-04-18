# 졸려
# 구현, 문자열, 시뮬레이션
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
s = input().strip()
word = [s]
while True:

    l = deque(s)
    r = deque()
    for i in range(len(s) // 2):
        r.append(l.pop())
    tmp = []

    while True:
        if not r:
            break

        tmp.append(l.popleft())
        tmp.append(r.popleft())

    if l:
        tmp.append(l.popleft())

    s = "".join(tmp)
    if s == word[0]:
        break
    word.append(s)

print(word)

# abcdef -> afbecd -> adfcbe -> aedbfc -> acefdb -> ... -> abcdef
# 깜박였을 때 모든 경우의 수에서
# -x만큼 뒤로 가면 원본 문자열 (n번 깜빡이기 전으로 돌아감)
# aedbfc는 3번 깜박였을 때,
print(word[-n % len(word)])
