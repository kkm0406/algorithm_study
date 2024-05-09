# 센서
# 그리디 알고리즘, 정렬

# n개의 센서들을 k개의 구간으로 분할
# 1, 6, 9, 3, 6, 7일 때 분할을 위해 오름차순 정렬
# 1, 3, 6, 6, 7, 9를 k개 구간으로 분할
# 수신 가능 영역 거리 합의 최솟값을 구하기 위해선
# 센서들간 거리가 가장 먼 순서대로 k-1개의 연결 고리를 제거해야 함
# 각 센서간 거리 차이는 2, 3, 0, 1, 2
# k가 2일 때 1개의 연결 고리만 제거하면 됨 -> 3
# -> 2, 0, 1, 2
# https://journeytosth.tistory.com/16
import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
dist = []
for i in range(1, n):
    dist.append(sensor[i] - sensor[i - 1])

dist.sort(reverse=True)
print(sum(dist[k - 1:]))

