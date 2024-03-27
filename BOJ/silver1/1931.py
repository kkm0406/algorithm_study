# 회의실 배정
# 그리디 알고리즘, 정렬
import sys

input = sys.stdin.readline
n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x: (x[1], x[0])) # 종료시간 기준 정렬
# 첫 번째 회의시간
s, e = time[0][0], time[0][1]
cnt = 1 # 첫 번째 회의포함
for i in range(1, n):
    # 마지막 회의 종료시간과 i번째 회의 시작시간 비교
    if time[i][0] >= e:
        s = time[i][0]
        e = time[i][1]
        cnt += 1

print(cnt)