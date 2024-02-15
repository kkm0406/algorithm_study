# AC
# 구현, 자료 구조, 문자열, 파싱, 덱

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()[1:-1].split(',')

    # n이 0인 경우에 arr == []
    if n == 0:
        # 빈 deq으로 초기화
        queue = deque()
    else:
        queue = deque(arr)

    cnt = 0
    flag = 0
    for i in p:
        # R의 개수가 홀수일 때만 뒤집기
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if len(queue) == 0:
                flag = 1
                print('error')
                break
            else:
                # 이전까지 R의 개수가 짝수였으면 popleft
                if cnt % 2 == 0:
                    queue.popleft()
                # R의 개수가 홀수면 뒤집어서 popleft -> pop
                else:
                    queue.pop()
    if flag == 0:
        # R의 개수에 따라 뒤집을지 말지 결정
        if cnt % 2 == 0:
            print('[' + ",".join(queue) + ']')
        else:
            queue.reverse()
            print('[' + ",".join(queue) + ']')