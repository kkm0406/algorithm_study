# 추월
# 구현, 자료 구조, 문자열, 해시를 사용한 집합과 맵
import sys

input = sys.stdin.readline
n = int(input())
start, end = {}, []

# 자동차가 들어간 순서 저장
for i in range(n):
    start[input().strip()] = i

for i in range(n):
    end.append(input().strip())

# 나오는 차를 순서대로 탐색
# 나온 차가 들어온 순서를 비교
# 현재 나온 차보다 먼저 들어간 차가 있는 경우 cnt + 1
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        #
        if start[end[i]] > start[end[j]]:
            cnt += 1
            break

print(cnt)