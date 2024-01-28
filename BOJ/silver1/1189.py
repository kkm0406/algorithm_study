# 컴백홈
# 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 깊이 우선 탐색, 백트래킹
import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
cnt = 0
visited = [[False] * c for _ in range(r)]
dir = ((1, 0), (-1, 0), (0, 1), (0, -1))


# dfs + 백트래킹
def dfs(x, y, dist):
    global cnt
    if x == 0 and y == c - 1:
        if dist == k:
            cnt += 1
    else:
        for i in range(4):
            dx, dy = x + dir[i][0], y + dir[i][1]
            # 이동 가능 범위
            if 0 <= dx < r and 0 <= dy < c:
                if not visited[dx][dy] and board[dx][dy] == ".":
                    # 방문 처리
                    visited[dx][dy] = True
                    dfs(dx, dy, dist + 1)
                    # 미방문 처리
                    visited[dx][dy] = False


# 출발지점 방문 처리
visited[r - 1][0] = True
dfs(r - 1, 0, 1)
print(cnt)
