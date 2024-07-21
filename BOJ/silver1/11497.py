# 통나무 건너뛰기
# 그리디 알고리즘, 정렬
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    left = []
    right = []

    # 높이 순으로 정렬하고
    # 가장 높은 나무가 가운데에 오고 i, i+1번째 나무가 각각 왼쪽, 오른쪽에 위치하도록
    for i in range(0, n - 1, 2):
        left.append(trees[i])
        right.append(trees[i + 1])

    if n % 2 == 0:
        result = left + sorted(right, reverse=True)
    else:
        result = left + [trees[-1]] + sorted(right, reverse=True)

    diff = -10e9
    for i in range(n - 1):
        diff = max(diff, abs(result[i] - result[i + 1]))

    diff = max(diff, abs(result[0] - result[-1]))

    print(diff)
