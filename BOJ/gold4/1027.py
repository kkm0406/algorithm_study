# 고층 건물
# 수학, 브루트포스 알고리즘, 기하학

import sys

input = sys.stdin.readline

n = int(input())
buildings = list(map(int, input().split()))
result = 0


def get_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


for idx, h in enumerate(buildings):
    cnt = 0
    # 현재까지 탐색한 건물 사이 기울기 최솟값보다 기울기가 더 작을 때 관측
    slope_l = sys.maxsize
    # 현재까지 탐색한 건물 사이 기울기 최댓값보다 기울기가 더 커질 때 관측
    slope_r = -sys.maxsize
    # 현재 건물 왼쪽 탐색
    for i in range(idx - 1, -1, -1):
        slope = get_slope(idx + 1, h, i + 1, buildings[i])
        if slope < slope_l: # 기울기가 더 작다면 관측 가능
            slope_l = slope
            cnt += 1
    # 현재 건물 오른쪽 탐색
    for i in range(idx + 1, n):
        slope = get_slope(idx + 1, h, i + 1, buildings[i])
        if slope > slope_r: # 기울기가 더 크다면 관측 가능
            slope_r = slope
            cnt += 1

    result = max(cnt, result)

print(result)
