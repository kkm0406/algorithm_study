# 팰린드롬 만들기
# 문자열, 브루트포스 알고리즘
from sys import stdin

input = stdin.readline

s = input().strip()
alpha = set(s)
if s == s[::-1]: # 이미 팰린드롬인 경우
    print(len(s))
else:
    # 원본 문자열이 qwerty일 때
    # trewq을 더해야 가장 길이가 긴 팰린드롬
    string = list(s[len(s)-2::-1])
    result = len(s)+len(string)
    while string:
        # 앞 문자를 제거하고
        string.pop(0)
        # 원본 문자열에 붙이기
        tmp = s+"".join(string)
        # 팰린드롬 여부 확인
        if tmp == tmp[::-1]:
            result = min(result, len(tmp))

    print(result)
