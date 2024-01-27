# 물병
# 수학, 그리디 알고리즘, 비트마스킹
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0
# 2진수의 1개수가 물통의 개수
# 13 -> 1101 : 8+4+1
while bin(n).count("1") > k:  # 1을 더했을 때 물통의 개수가 k보다 클 떄까지
    n += 1  # 물통을 하나씩 추가
    cnt += 1

print(cnt)
