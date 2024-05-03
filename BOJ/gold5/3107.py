# IPv6
# 구현, 문자열
import sys

input = sys.stdin.readline

addr = input().strip().split(":")
if addr[0] == "":  # ex) ::1
    addr = addr[1:]
if addr[-1] == "":  # ex)1::
    addr = addr[:-1]

result = ""
for i in range(len(addr)):
    # ::인 경우
    # ip주소에서 필요한 만큼 0000을 붙임
    if addr[i] == "":
        result += "0000:" * (8 - len(addr) + 1)
    # 0이 생략된 만큼 추가
    else:
        tmp = ""
        for j in range(4 - len(addr[i])):
            tmp += "0"
        result += tmp + addr[i] + ":"

print(result[:-1])
