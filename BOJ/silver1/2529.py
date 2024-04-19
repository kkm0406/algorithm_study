# 부등호
# 브루트포스 알고리즘, 백트래킹
import sys

input = sys.stdin.readline

k = int(input())
s = list(input().strip())
tmp = ""
for i in s:
    if i == "<" or i == ">":
        tmp += i
s = tmp

visited = [False] * 10
result = []


def check(prev, now, ops):
    if ops == "<":
        if prev < now:
            return True
        else:
            return False
    elif ops == ">":
        if prev > now:
            return True
        else:
            return False


def dfs(depth, nums):
    if depth == k + 1:
        # print(nums)
        result.append(nums)
        return

    for i in range(10):
        if not visited[i]:
            if not nums or check(nums[-1], str(i), s[depth - 1]):
                visited[i] = True
                dfs(depth + 1, nums + str(i))
                visited[i] = False


dfs(0, "")
print(max(result))
print(min(result))
