# 선발 명단
# 브루트포스 알고리즘, 백트래킹
import sys

input = sys.stdin.readline


def dfs(depth, pick, visited, team):
    global result
    if depth == 11:
        result = max(result, sum(pick))
    else:
        for i in range(11):
            # depth번째 선수의 포지션을 정하는 경우
            if not visited[i] and team[depth][i] != 0:
                visited[i] = True
                pick.append(team[depth][i])
                dfs(depth + 1, pick, visited, team)
                visited[i] = False
                pick.pop()


for _ in range(int(input())):
    team = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    result = 0
    dfs(0, [], visited, team)
    print(result)
