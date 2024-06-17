# 팰린드롬 만들기
# 구현, 그리디 알고리즘, 문자열
import sys
from collections import defaultdict

input = sys.stdin.readline

s = input().strip()
alpha = defaultdict(int)
for i in s:
    alpha[i] += 1

# 알바펫 순 오름차순 정렬
arr = sorted(alpha.items(), key=lambda x: x[0])
# 순서대로 l과 r에 추가해서 최종적으로 l+r 문자열 구성
l, r = "", ""

# 처음 팰린드롬 만들고 남은 알파벳
left = {}
for item in arr:
    # 알바펫 개수가 두 개 이상이면
    # l과 r에 동일한 개수만큼 분배
    if item[1] >= 2:
        l = l + item[0] * (item[1] // 2)
        r = r + item[0] * (item[1] // 2)
        # l과 r에 분배 후 남은 알파벳
        left[item[0]] = item[1] - (item[1] // 2) * 2
    else:
        left[item[0]] = item[1]

# 나머지 알파벳을 l과 r사이 추가하며 팰린드롬 생성
cnt = 0
for key, value in left.items():
    if value == 1:
        cnt += 1
        # 남은 알파벳이 2개 이상인 경우 break
        # ex) AABCAA
        if cnt > 1:
            print("I'm Sorry Hansoo")
            exit()
        # 남은 알파벳 추가
        l += key

print(l+r[::-1])
