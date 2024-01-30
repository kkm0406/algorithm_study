# 차트
# 브루트포스 알고리즘
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
answer = 0


def check(nums):
    line = [nums[0]]
    result = 0
    # 각 라인이 어느 포인트에 그려지는 지 추가
    for i in range(1, n):
        line.append(line[-1] + nums[i])
    # 라인끼리 50을 만들 수 있는 경우면 result + 1
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if abs(line[i] - line[j]) == 50:
                result += 1
    return result


# 최댓값이 50보다 크면 원 중심 지나는 경우 없음
if max(arr) > 50:
    print(0)
# 최댓값이 50이면 원 중심 지나는 경우 무조건 하나
elif max(arr) == 50:
    print(1)
else:
    # 원 그래프를 그리는 모든 경우의 수
    # 시계 방향으로 차트를 그릴 때
    perms = list(permutations(arr))
    for p in perms:
        answer = max(answer, check(p))
    print(answer)
