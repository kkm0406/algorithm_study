# 안정적인 문자열

import sys

input = sys.stdin.readline
idx = 1
while True:
    s = input().strip()
    if "-" in s:
        break
    st = []
    # 입력 문자열에서 안정적인 문자열 제거
    for i in range(len(s)):
        if not st:
            st.append(s[i])
        else:
            if s[i] == "{":
                st.append(s[i])
            else:
                if st[-1] == "{":
                    st.pop()
                else:
                    st.append(s[i])
    string = "".join(st)
    cnt = 0
    # {{인 경우 연산 + 1 하고 {{ 제거
    cnt += string.count("{{")
    string = string.replace("{{", "")
    # }}인 경우 연산 + 1 하고 }} 제거
    cnt += string.count("}}")
    string = string.replace("}}", "")
    # 빈 문자열이면 출력
    if not string:
        print("%d. %d" % (idx, cnt))
    # 문자열이면 }{인 경우 밖에 없음
    # }{인 경우 연산 + 2
    else:
        cnt += (string.count("}{") * 2)
        print("%d. %d" % (idx, cnt))

    idx += 1
