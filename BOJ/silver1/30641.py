# 회문 끝말잇기
# 수학, 조합론, 게임 이론
import sys

input = sys.stdin.readline

L, U = map(int, input().split())
MOD = 10 ** 9 + 7
sum_palindromes = 0
multi = 1

if L == 1:  # 1에서 시작
    sum_palindromes += 1
    L += 1

if U != 1 and L == 2:  # 1에서 끝이 안 나고 2에서 시작
    sum_palindromes += 1
    L += 1

# 이후 더해지는 값은 모두 짝수이기에 지금 홀수여야 호영이의 승리
print("H" if sum_palindromes % 2 == 1 else "A")

for i in range(3, U + 1):
    if i % 2 == 1:  # 2칸마다 26을 곱해준다.
        multi = (multi * 26) % MOD
    if i >= L:  # 범위 안에 있을 경우
        sum_palindromes = (sum_palindromes + multi) % MOD

print(sum_palindromes)
