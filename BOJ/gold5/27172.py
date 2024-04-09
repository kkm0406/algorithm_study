# 수 나누기 게임
# 수학, 브루트포스 알고리즘, 정수론, 소수 판벙, 에라토스테네스의 체
import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
max_num = max(x)
score = [0 for _ in range(max_num + 1)]
set_x = set(x)
for i in x:
    if i == max_num:
        continue
    # 에라스토테네스의 체에서 특정 소수의 배수들을 제하는 과정 응용
    # 어떤 수의 배수들에 대해 게임 진행
    for j in range(2 * i, max_num + 1, i):
        if j in set_x:  # 숫자 집합에 있으면
            score[i] += 1
            score[j] -= 1

for i in x:
    print(score[i], end=" ")
