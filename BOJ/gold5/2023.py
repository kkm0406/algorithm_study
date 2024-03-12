# 신기한 소수
# 수학, 정수론, 백트래밍, 소수 판정
import sys
import math

input = sys.stdin.readline
n = int(input())
# 소수가 될 수 있는 숫자들(짝수는 안됨)
nums = [1, 2, 3, 5, 7, 9]
# 가장 왼쪽의 숫자는 무조건 소수
start = [2, 3, 5, 7]
arr = []


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
        if num % i == 0:
            return False

    return True


def dfs(depth, pick):
    if depth == n:
        arr.append(pick)

    else:
        for i in range(6):
            # 앞에 1이 오는 경우 continue
            if not pick and nums[i] not in start:
                continue

            # 새로운 숫자가 들어오면 소수 판별
            if is_prime(int(pick + str(nums[i]))):
                dfs(depth + 1, pick + str(nums[i]))


dfs(0, "")
for i in sorted(arr):
    print(i)
