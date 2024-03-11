# 센티와 마법의 뿅망치

import sys, heapq

input = sys.stdin.readline

n, centi, t = map(int, input().split())
h = []
flag = False
for _ in range(n):
    a = int(input())
    heapq.heappush(h, -a)

idx = 0
while True:
    if idx == t:
        break

    # 가장 큰 거인
    top = -1 * heapq.heappop(h)
    # 가장 큰 거인의 키가 센티보다 작은 경우
    if top < centi:
        print("YES")
        print(idx)
        exit()

    if top <= 1:
        heapq.heappush(h, -1 * top)
    else:
        top //= 2
        heapq.heappush(h, -1 * top)
    idx += 1

# 뿅망치 다 썼을 때
# 가장 큰 거인의 키
top = -1 * heapq.heappop(h)
if top < centi:
    print("YES")
    print(idx)
else:
    print("NO")
    print(top)
