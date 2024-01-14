# 부분수열의 합
# 브루트포스 알고리즘, 백트래킹

import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
nums = []


# 백트래킹
def dfs(depth):
    global cnt
    if sum(nums) == s and len(nums) > 0:
        cnt += 1
    # depth부터 끝까지
    for i in range(depth, n):
        # 현재 원소를 추가
        nums.append(arr[i])
        # 재귀 진행
        dfs(i + 1)
        # 현재 원소 제거
        nums.pop()


dfs(0)
print(cnt)
