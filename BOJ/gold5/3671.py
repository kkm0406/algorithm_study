# 산업 스파이의 편지
# 수학, 브루트포스 알고리즘, 정수론, 조합론, 소수 판정, 에라토스테네스의 체
import math
import sys
from itertools import permutations

input = sys.stdin.readline
c = int(input())


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


for _ in range(c):
    n = list(map(int, input().strip()))
    perms = []
    for i in range(1, len(n) + 1):
        perms += list(permutations(n, i))

    arr = set()
    for perm in perms:
        number = int("".join(list(map(str, perm))))
        if is_prime(number):
            arr.add(number)

    print(len(arr))
