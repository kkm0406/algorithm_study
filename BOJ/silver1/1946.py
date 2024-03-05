# 신입 사원
# 그리디 알고리즘, 정렬
import sys

input = sys.stdin.readline

# 자신보다 서류, 면접 모두 등수가 낮은 인원 탈락
# a: 1등, 2등  / b: 2등, 3등이면 b는 탈락
for _ in range(int(input())):
    n = int(input())
    score = []
    for i in range(n):
        a, b = map(int, input().split())
        score.append([a, b])
    # 우선 서류 기준 정렬
    score.sort(key=lambda x: x[0])
    # 서류 1등은 무조건 합격
    cnt = 1
    # 이전 합격자의 면접 등수
    prev = score[0][1]
    for i in range(1, n):
        # 이전 합격자보다 등수가 낮으면
        if prev > score[i][1]:
            # 합격 대상
            cnt += 1
            # 면접 등수 초기화
            prev = score[i][1]
    print(cnt)
