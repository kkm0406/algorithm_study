# DNA 비밀번호
# 문자열, 슬라이딩 윈도우

import sys

input = sys.stdin.readline

s, p = map(int, input().split())
dna = input().strip()
a, c, g, t = map(int, input().split())
# 비밀번호 내 a, c, g, t 개수
dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
l, r = 0, p - 1
cnt = 0
#초기 비밀번호
init_pw = dna[l:r + 1]
for i in init_pw:
    dic[i] += 1


while r < s:
    # 최소 기준 통과 시
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        cnt += 1
    # 한 칸 이동해서 탐색
    # 맨 왼쪽 알파벳 개수 -1
    dic[dna[l]] -= 1
    # 오른쪽으로 한 칸 씩 이동
    l += 1
    r += 1
    # 인덱스 에러 방지
    if r < s:
        # 새로운 알파벳 추가
        dic[dna[r]] += 1

print(cnt)
