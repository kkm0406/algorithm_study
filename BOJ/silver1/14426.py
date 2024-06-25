# 접두사 찾기
# 자료 구조, 문자열, 트리, 이분 탐색, 트라이
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = set()

# 각 문자열에서 접두사 가 될 수 있는 모든 경우를 집합에 추가
for i in range(n):
    s = input().strip()
    tmp = ""
    # 빈 문자열에서 계속 문자를 더함
    for j in range(len(s)):
        tmp += s[j]
        arr.add(tmp)


cnt = 0

for _ in range(m):
    check = input().strip()
    if check in arr:
        cnt += 1

print(cnt)