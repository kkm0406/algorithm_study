# 순열의 순서
# 수학, 구현, 조합론
import math
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
nums = [i for i in range(1, n + 1)]
if arr[0] == 1:
    # n=5, k=35 일 때
    # n! = 120, 120//5 = 24이므로, 이는 각각의 앞자리 5개가 가지는 경우의 수
    # 앞자리가 1인 경우: 1~24번째, 앞자리가 2인 경우: 25~48번째, ...
    # k가 35이면, 앞자리가 2인 경우
    # 다음 단계로 넘어가면 n = 4, k = 35-24 = 11
    # -> 맨 앞자리가 2일 때 11번째 수열 찾기
    # 이 과정을 반복
    idx = arr[1]
    result = []
    for i in range(n, 0, -1):
        fac = math.factorial((i - 1))
        step = (idx - 1) // fac
        result.append(nums[step])
        del nums[step]
        idx -= fac * step
    print(*result)
else:
    # n = 5, k = 2, 3, 5, 1, 4일 때
    # n = 5, 5! = 120, 120/n = 24이다
    # 맨 앞자리가 2이므로 25 ~ 48에 포함 + 24
    # 그 다음 3이므로 다음 7 ~ 12에 포함 + 5
    # 이 과정을 반복하여 모두 더함
    arr = arr[1:]
    idx = 1
    for i in range(n, 0, -1):
        fac = math.factorial(i - 1)
        step = nums.index(arr[n - i])
        del nums[step]
        idx += fac * step
    print(idx)
