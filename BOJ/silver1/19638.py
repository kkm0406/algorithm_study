# 센티와 마법의 뿅망치
# 구현, 자료구조, 우선순위 큐
import sys, heapq

input = sys.stdin.readline

n, centi, t = map(int, input().split())
h = []
flag = False
for _ in range(n):
    a = int(input())
    heapq.heappush(h, -a)

# 센티보다 큰 거인이 있으면 False 반환
# 그렇지 않으면 True 반환
def check():
    for i in h:
        if -1 * i >= centi:
            return False
    return True


if check():
    print("YES")
    print(0)
    exit()
else:
    for i in range(1, t + 1):
        # 가장 큰 거인
        top = -1 * heapq.heappop(h)
        if top == 1:
            heapq.heappush(h, -1 * top)
        else:
            heapq.heappush(h, -1 * (top // 2))

        # 센티와 거인들 키 비교
        if check():
            print("YES")
            print(i)
            break
    # 다 때리고도 센티보다 큰 거인이 있을 때
    else:
        print("NO")
        print(-1 * heapq.heappop(h))
