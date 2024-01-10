# 키로거
# 자료 구조, 스택, 연결리스트

import sys
from collections import deque
input = sys.stdin.readline


for _ in range(int(input())):
    # 커서 위치에 따라 입력을 다르게 저장하기 위해 deque를 두 개 선언
    # left는 기본적으로 문자를 저장 및 삭제하는 deque
    left, right = deque(), deque()
    key = input().strip()
    for i in range(len(key)):
        # 왼쪽 커서일 때
        if key[i] == "<":
            if left:
                # left의 마지막 원소를 right에 삽입
                right.appendleft(left.pop())
        # 오른쪽 커서일 때
        elif key[i] == ">":
            if right:
                # right의 첫 번째 원소를 left에 삽입
                left.append(right.popleft())
        elif key[i] == "-":
            if left:
                left.pop()
        else:
            left.append(key[i])

    answer1 = "".join(left)
    answer2 = "".join(right)
    print(answer1+answer2)

