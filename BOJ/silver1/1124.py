# 언더프라임
# 수학, 정수론, 소수 판정, 에라스토테네스의 체
import sys

input = sys.stdin.readline

a, b = map(int, input().split())

primes = [False, False] + [True] * (100000 - 1)

for i in range(2, 100001):
    if primes[i]:
        for j in range(i * 2, 100001, i):
            primes[j] = False

cnt = 0


def under_prime(n):
    tmp = 0
    num = n
    # 시간 초과 때문에 int(n ** (0.5)) + 1까지 탐색
    for i in range(2, int(n ** (0.5)) + 1):
        if primes[i] and n % i == 0:
            while True:
                num = num // i
                tmp += 1
                if num % i != 0:
                    break

    # 남은 수가 소수인 경우
    if primes[num]:
        tmp += 1
    return tmp


for i in range(a, b + 1):
    if primes[i]:
        continue

    result = under_prime(i)
    if primes[result]:
        cnt += 1

print(cnt)
