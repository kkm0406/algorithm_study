# 압축
# 자료 구조, 스택, 재귀
import sys

input = sys.stdin.readline

s = input().strip()
idx = []
result = 0
num = 0
cnt = 0
for i in range(len(s)):
    if s[i] == "(":
        # '('전의 길이, 곱해야할 값 저장
        idx.append([cnt-1, num])
        # '(' 이후부터 개수 다시 셈
        cnt = 0
    elif s[i] == ")":
        prev_len, prev_num = idx.pop()
        # 해당 개수만큼 곱하고 이전까지의 길이 더함
        cnt = cnt * prev_num + prev_len
    else:
        # 길이 + 1
        cnt += 1
        # 곱해야할 값
        num = int(s[i])

print(cnt)
