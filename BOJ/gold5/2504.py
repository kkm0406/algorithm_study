# 괄호의 값
# 구현, 자료 구조, 스택

# 초기 값을 1로 설정
# (가 열릴 때 2를 곱하고
# [가 열릴 때 3을 곱한고
# ), ]가 닫힐 땐 //2, //3
# (), [] 처럼 열고 바로 닫히는 경우, 결과 값에다 덧셈
import sys

input = sys.stdin.readline
s = input().strip()
st = []
answer = 0
tmp = 1
for i in range(len(s)):
    if s[i] == "(":
        st.append(s[i])
        tmp *= 2
    elif s[i] == "[":
        st.append(s[i])
        tmp *= 3
    elif s[i] == ")":
        if not st or st[-1] == "[":
            print(0)
            exit()
        if s[i - 1] == "(":
            answer += tmp
        st.pop()
        tmp //= 2
    elif s[i] == "]":
        if not st or st[-1] == "(":
            print(0)
            exit()
        if s[i - 1] == "[":
            answer += tmp
        st.pop()
        tmp //= 3

if st:
    print(0)
else:
    print(answer)
