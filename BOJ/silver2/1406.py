# 에디터
# 자료 구조, 스택, 연결 리스트
from sys import stdin
from collections import deque

input = stdin.readline

# 커서 왼쪽에 있는 문자
l = deque(input().strip())
# 커서 오른쪽에 있는 문자
r = deque()
m = int(input())
for _ in range(m):
    ops = input().strip()
    # 커서를 왼쪽이동 -> 커서의 오른쪽에 있는 문자를 r에 저장
    # : l의 마지막 문자을 r에 이동
    if ops[0] == "L":
        if l:
            r.appendleft(l.pop())
    # 커서 오른쪽이동 -> 커서의 왼쪽에 있는 문자를 l에 저장
    elif ops[0] == "D":
        if r:
            l.append(r.popleft())
    elif ops[0] == "B":
        if l:
            l.pop()
    else:
        l.append(ops[-1])

print("".join(l) + "".join(r))
