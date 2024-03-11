# 계란으로 계란치기
# 브루트포스 알고리즘, 백트래킹
import sys

input = sys.stdin.readline
n = int(input())

# 내구도, 무게
egg = [list(map(int, input().split())) for _ in range(n)]
result = 0


def dfs(depth):
    global result

    # 가장 오른쪽 계란 도착
    if depth == n:
        cnt = 0
        # 모든 계란 탐색하면서
        for v, w in egg:
            # 깨진 계란 카운트
            if v <= 0:
                cnt += 1

        result = max(result, cnt)
        return

    # 현재 인덱스의 계란이 깨져있으면
    if egg[depth][0] <= 0:
        # 오른쪽 이동
        dfs(depth + 1)
        return

    # 현재 인덱스의 계란 외에 모든 계란이 깨져있는지 확인
    for i in range(n):
        if i == depth:
            continue
        if egg[i][0] > 0:
            break
    else:
        result = max(result, n - 1)
        return

    # 계란 깰 수 있으면 깨고 백트래킹
    for i in range(n):
        if i == depth or egg[i][0] <= 0:
            continue
        egg[depth][0] -= egg[i][1]
        egg[i][0] -= egg[depth][1]
        dfs(depth + 1)
        egg[depth][0] += egg[i][1]
        egg[i][0] += egg[depth][1]


dfs(0)
print(result)
