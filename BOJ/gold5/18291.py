# 비요뜨의 징검다리 건너기
# 수학, 조합론, 분할 정복을 이용한 거듭제곱

# n이 1, 2일 때 건너는 방법은 1
# n이 3 이상일 경우 2 ~ n-1번 돌을 밟거나 밟지 않거나 -> 2^(n-2) 경우의 수
# n이 짝수인 경우 get_pow(x)*get_pow(x)를 mod로 나눈 나머지는
# get_pow(x)를 mod로 나눈 나머지와 동일
# n이 홀수인 경우 2*get_pow(x)*get_pow(x)를 mod로 나눈 나머지가
# get_pow(x)를 mod로 나눈 나머지와 동일
import sys

input = sys.stdin.readline
mod = 10 ** 9 + 7

# 2의 b 제곱을 mod로 나눈 나머지를 반환하는 함수
def get_pow(b):
    a = 2
    result = 1
    while b:
        if b % 2 != 0:
            result = (result * a) % mod
        b //= 2
        a = (a * a) % mod
    return result


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(get_pow(n - 2))
