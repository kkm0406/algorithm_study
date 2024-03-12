# 나무꾼 이다솜
# 구현, 브루트포스 알고리즘
import sys

input = sys.stdin.readline

n, c, w = map(int, input().split())
trees = [int(input()) for _ in range(n)]
ans = 0

# 자를 나무의 길이
for i in range(1, max(trees) + 1):
    result = 0
    for tree in trees:
        # 나무의 길이를 i로 나누었을 때
        cnt, remain = divmod(tree, i)
        # 나머지가 생기면 자를 횟수는 몫
        if remain:
            cost = c * cnt
        # 나머지가 안생기면 자르는 횟수는 몫-1
        else:
            cost = c * (cnt - 1)

        # 자른 나무 비용
        sell = (cnt * i * w) - cost

        if sell < 0:
            continue

        # 이익 추가
        result += sell

    ans = max(ans, result)

print(ans)
