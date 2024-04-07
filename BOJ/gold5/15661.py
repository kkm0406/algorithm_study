# 링크와 스타트
# 브루트포스 알고리즘, 비트마스킹, 백트래킹
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
nums = [1 for i in range(n)]
result = sys.maxsize


def dfs(depth):
    global result
    if depth == n:
        if sum(nums) == 0 or sum(nums) == n:
            return
        start, link = 0, 0
        # 전체 돌면서
        for i in range(n):
            for j in range(n):
                # i와 j가 모두 선택 -> 스타트팀 배정
                if nums[i] and nums[j]:
                    start += arr[i][j]
                # 모두 선택 못받으면 -> 링크팀 배정
                elif not nums[i] and not nums[j]:
                    link += arr[i][j]

        result = min(result, abs(start - link))
        return

    # for문 안쓰고 백트래킹
    nums[depth] = 1
    dfs(depth + 1)
    nums[depth] = 0
    dfs(depth + 1)


dfs(0)
print(result)
