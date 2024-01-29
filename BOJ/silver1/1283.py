# 단축키 지정
# 구현, 문자열

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    word = input().strip()
    # 공백 기준 분리
    tmp = word.split()

    for j in range(len(tmp)):
        # 단어의 첫 글자가 단축키가 아닐 때
        if tmp[j][0].lower() not in arr and tmp[j][0].upper() not in arr and tmp[j][0] != " ":
            # 단축키에 포함
            arr.append(tmp[j][0])
            tmp[j] = list(tmp[j])
            # 해당 글자에 []씌움
            tmp[j][0] = "[" + tmp[j][0] + "]"
            tmp[j] = "".join(tmp[j])
            print(" ".join(tmp))
            break
    # 모든 단어의 첫 글자가 단축키일 때
    else:
        for j in range(len(word)):
            # 단축키 미지정 글자를 찾음
            if word[j].upper() not in arr and word[j].lower() not in arr and word[j] != " ":
                arr.append(word[j])
                word = word[:j] + "[" + word[j] + "]" + word[j + 1:]
                print(word)
                break
        # 어떤 것도 단축키 지정 못하는 경우
        else:
            arr.append("-")
            print(word)
