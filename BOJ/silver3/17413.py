# 단어 뒤집기 2
# 구현, 자료구조, 문자열, 스택

import sys

input = sys.stdin.readline
sentence = input().strip()
tag = []
for i in range(len(sentence)):
    # 스택이 비어있으면 추가
    if not tag:
        tag.append(sentence[i])
    else:
        # >를 만나면 원본 출력 후 스택 클리어
        if sentence[i] == ">":
            tag.append(sentence[i])
            print("".join(tag), end="")
            tag.clear()
        # <일 때
        elif sentence[i] == "<":
            # 이미 스택에 문자가 있으면
            if tag:
                # 역순 출력 후 스택 클리어
                print("".join(tag[::-1]), end="")
                tag.clear()
            # 스택에 문자 추가
            tag.append(sentence[i])
        # 공백일 때
        elif sentence[i] == " ":
            # <으로 시작하는 문자열이면 그냥 추가
            if tag[0] == "<":
                tag.append(sentence[i])
            # 아니면 역순 출력 후 스택 클리어
            else:
                print("".join(tag[::-1]), end=" ")
                tag.clear()
        # 스택에 추가
        else:
            tag.append(sentence[i])

# 문자열 순회 후 스택에 문자가 있으면 역순 출력
if tag:
    print("".join(tag[::-1]), end="")
