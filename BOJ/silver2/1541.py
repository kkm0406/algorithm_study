# 잃어버린 괄호
# 수학, 그리디 알고리즘, 문자열, 파싱

import sys
input = sys.stdin.readline

s = input().strip()
result = []

# '-' 기준 분리하고 '+'끼리 더함
# ex) 5-6+7-8+9 -> 5-(5+6)-(8+9)
s = s.split("-")

for i in range(len(s)):
    # s[i]는 '+'가 있는 식
    # '+'기준으로 분리하고 각 원소 형변환 수 더함
    tmp = s[i].split("+")
    tmp = map(int, tmp)
    result.append(sum(tmp))

# 앞에서부터 -연산
answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]

print(answer)


