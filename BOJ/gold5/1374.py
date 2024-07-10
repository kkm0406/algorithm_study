# 강의실
# 자료 구조, 그리지 알고리즘, 정렬, 우선순위 큐
import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 시작 시간 기준 정렬
arr.sort(key=lambda x: (x[1], x[2], x[0]))
q = []  # 강의 종료 시간 기준 우선순위 큐
heapq.heappush(q, arr[0][-1])  # 가장 처음 시작하는 강의의 종료 시간

for i in range(1, n):
    idx, s, e = arr[i]
    if q[0] > s:  # i번째 강의의 시작시간이 가장 빨리 끝나는 강의보다 빠르면
        heapq.heappush(q, e)  # 새로운 강의실 배정
    else:
        heapq.heappop(q)  # 가장 빨리 끝나는 강의 pop
        heapq.heappush(q, e)  # 해당 강의실에 추가

print(len(q))
