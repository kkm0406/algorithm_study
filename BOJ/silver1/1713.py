# 후보 추천하기
# 구현, 시뮬레이션

import sys

input = sys.stdin.readline

m = int(input())
n = int(input())
std = list(map(int, input().split()))
pic = {} # 학생 이름: [득표수, 인덱스]
for i in range(n):
    # 현재 사진이 게시된 학생이 다른 학생의 추천을 받는 경우
    if std[i] in pic:
        pic[std[i]][0] += 1
    else:
        # 사진틀이 비어있을 때
        if len(pic) < m:
            pic[std[i]] = [0, i]
        # 비어있는 사진틀이 없는 경우
        else:
            # 추천수, 인덱스 기준으로 정렬
            tmp = sorted(list(pic.items()), key=lambda x: (x[1][0], x[1][1], x[0]))
            # 역순으로 바꾼 후 맨 마지막 원소 제거
            tmp = list(reversed(tmp))
            tmp.pop()
            pic = dict(tmp)
            # 새로운 학생 추천
            pic[std[i]] = [0, i]

print(*sorted(pic.keys()))
