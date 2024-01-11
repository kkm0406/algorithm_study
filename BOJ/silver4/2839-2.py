# 설탕 배달
# 수학, 다이나믹 프로그래밍, 그리디 알고리즘

import sys

input = sys.stdin.readline

n = int(input())
cnt = 0

while n >= 0:
    # 무게가 5로 나누어 떨어지면 개수 세고 종료
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    # 매 반복마다 3씩 나누고 개수 + 1
    n -= 3
    cnt += 1
else:
    print(-1)
