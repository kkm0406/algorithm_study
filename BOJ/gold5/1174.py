# 줄어드는 수

import sys

input = sys.stdin.readline

n = int(input())

cnt = 1

nums = [i for i in range(9, -1, -1)]
visited = [False] * 10
check = []
result = []


def dfs(depth):

    if check:
        result.append(int("".join(map(str, check))))

    for i in range(depth, 10):
        if not visited[i]:
            if not check:
                visited[i] = True
                check.append(nums[i])
                dfs(depth + 1)
                visited[i] = False
                check.pop()
            else:
                if nums[i] < check[-1]:
                    visited[i] = True
                    check.append(nums[i])
                    dfs(depth + 1)
                    visited[i] = False
                    check.pop()


dfs(0)
result.sort()
result = [-1] + result
if n >= len(result):
    print(-1)
else:
    print(result[n])

