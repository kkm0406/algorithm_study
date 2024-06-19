# 팔
# 수학, 그리디 알고리즘
import sys

input = sys.stdin.readline

l, r = input().split()

# 둘이 길이가 다른 경우
# ex) 88 888 -> 8없는 경우 무조건 존재
if len(r) != len(l):
    print(0)
else:
    cnt = 0
    # 앞에서부터 숫자 비교
    for i in range(len(r)):
        # 숫자가 다른 경우 뒤에는 더 안봐도 됨
        # ex) 8880, 8808 -> '80'과 '08'사이 8없는 경우 존재
        if r[i] != l[i]:
            break
        # 숫자가 모두 '8'인 경우 cnt + 1
        elif r[i] == '8' and l[i] == '8':
            cnt += 1
        # 숫자가 같지만 '8'이 아닌 경우 탐색 진행
        else:
            continue

    print(cnt)
