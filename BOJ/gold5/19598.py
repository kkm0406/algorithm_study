# 최소 회의실 개수
# 자료 구조, 그리지 알고리즘, 정렬, 스위핑, 우선순위 큐
import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 시작시간 기준 정렬
arr.sort()

q = []
# 가장 빨리 시작하는 회의를 넣음
heapq.heappush(q, arr[0][1])

for i in range(1, n):
    #i번째 회의의 시작/종료시간
    s, e = arr[i]
    # 회의 시작이 더 빠르면 -> 새로운 회의실 배정
    if q[0] > s:
        heapq.heappush(q, e)
    else:
        # 해당 회의에 뒤이어서
        heapq.heappop(q)
        heapq.heappush(q, e)

print(len(q))
