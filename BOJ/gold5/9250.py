# 맥주 마시면서 걸어가기
# 그래프 이론, 그래프 탐색, 너비 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())


def bfs():
    # 시작점
    q = deque([[home[0], home[1]]])


    while q:
        x, y = q.popleft()
        # 현재 위치로 부터 페스티벌 갈 수 있는 경우
        if abs(x - festival[0]) + abs(y - festival[1]) <= 20 * 50:
            print('happy')
            return

        # 편의점 방문
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x - nx) + abs(y - ny) <= 20 * 50:
                    visited[i] = True
                    q.append([nx, ny])

    print('sad')
    return


for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))
    beer = 20
    visited = [False] * (n + 1)
    bfs()
