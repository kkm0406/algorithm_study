# 카드 정렬하기
# 자료 구조, 그리디 알고리즘, 우선순위 큐
import heapq
import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
card = []
for i in arr:
    heapq.heappush(card, i)

result = []
# 값이 가장 작은 애들 두명씩 더하기
while len(card) >= 2:
    a = heapq.heappop(card)
    b = heapq.heappop(card)

    tmp = a+b
    result.append(tmp)
    heapq.heappush(card, tmp)

print(sum(result))
