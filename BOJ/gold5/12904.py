# A와 B
# 구현, 그리디 알고리즘, 문자열
import sys

input = sys.stdin.readline

s = input().strip()
t = input().strip()

s = list(s)
t = list(t)

# 연산을 통해 t를 s로 바꿈
while len(t) > len(s):
    # 마지막 글자가 A이면 A 제거
    if t[-1] == "A":
        t.pop()
    # 마지막 글자가 B면 B제거 후 문자열 뒤집기
    elif t[-1] == "B":
        t.pop()
        t = t[::-1]

print(1 if t == s else 0)
