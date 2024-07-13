# 머리 톡톡
# 수학, 정수론, 소수 판정
import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
size = 1000000
nums = [0] * (size + 1)  # 입력한 숫자가 등장한 개수
cnt = [0] * (size + 1)  # i번째 숫자를 치는 횟수를 저장
for i in arr:
    nums[i] += 1

# 에라스토테네스의 체 응용
for i in range(1, size + 1):
    if nums[i]:  # 숫자가 등장했으면
        cnt[i] += nums[i] - 1  # 자기자신은 머리를 치는 횟수에 포함x
        for j in range(i * 2, size + 1, i):  # i의 배수를 탐색
            cnt[j] += nums[i]  # i번 숫자가 등장한 횟수만큼 더해줌

for i in arr:
    print(cnt[i])
