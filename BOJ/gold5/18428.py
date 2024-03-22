# 감시 피하기
# 브루트포스 알고리즘, 백트래킹
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
arr = [list(input().split()) for i in range(n)]
tmp = []
tchr = []
std = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "X":
            tmp.append([i, j])
        elif arr[i][j] == "T":
            tchr.append([i, j])
        elif arr[i][j] == "S":
            std.append([i, j])

# 장애물을 세울 수 있는 좌표 조합
combs = list(combinations(tmp, 3))


# 장애물 설치 / 해체
def barrier(comb, mode):
    for i in comb:
        if mode == 1:
            arr[i[0]][i[1]] = "O"
        else:
            arr[i[0]][i[1]] = "X"


for comb in combs:
    barrier(comb, 1)
    flag = True
    # 선생님들 기준
    for t in tchr:
        # 동서남북 한 방향에서
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = t[0], t[1]
            # 한 방향으로 쭉 이동
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < n and 0 <= ny < n:
                    # 학생이 보이면 해당 장애물 조합은 실패
                    if arr[nx][ny] == "S":
                        flag = False
                        break
                    if arr[nx][ny] == "O":
                        break
                else:
                    break

    barrier(comb, 2)

    # 학생을 못보는 경우가 있을 때
    if flag:
        print("YES")
        break
else:
    print("NO")
