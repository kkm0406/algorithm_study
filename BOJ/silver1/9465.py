# 스티커
# 다이나믹 프로그래밍
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())), list(map(int, input().split()))]
    for i in range(1, n):
        if i == 1:
            arr[0][i] += arr[1][i - 1]
            arr[1][i] += arr[0][i - 1]
        else:
            # 이전 열의 대각선 위치 vs 이전 이전 열의 대각선 위치
            arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])

    print(max(arr[0][-1], arr[1][-1]))
