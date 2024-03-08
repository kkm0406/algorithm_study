# 회문
# 문자열, 두 포인터
import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    s = list(input().strip())
    l, r = 0, len(s) - 1
    flag = True
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            # l번째 문자와 r번째 문자가 다를 때
            # ex) summuus에서
            # l, r이 2, 4일 때
            # s1 = s[3:5] = mu -> l+1 인덱스부터 다시 확인
            # s2 = s[2:4] = mm -> r-1 인덱스부터 회문 확인
            s1 = s[l+1:r+1]
            s2 = s[l:r]
            # 둘 중 하나가 회문일 때
            if s1 == s1[::-1] or s2 == s2[::-1]:
                print(1)
                break
            else:
                print(2)
                break
    else:
        print(0)


