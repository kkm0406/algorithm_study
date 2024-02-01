# KCPC
# 구현, 정렬
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    team = {}  # cnt, last
    score = {}  # 팀의 문제별 점수
    for i in range(m):
        id, num, s = map(int, input().split())
        if id not in team:
            team[id] = [1, i]  # 제출 횟수, 제출 시간
            score[id] = [0] * (k + 1)  # 문제별 점수
            score[id][num] = s
        else:
            team[id][0] += 1
            team[id][1] = i
            score[id][num] = max(s, score[id][num])

    # 제출 횟수, 제출 시간 딕셔너리에 최종 점수 추가
    for id, s in score.items():
        team[id].append(sum(s))

    # 조건에 따라 오름차순 정렬
    result = list(team.items())
    result.sort(key=lambda x: (x[1][2], -x[1][0], -x[1][1]))
    # 다시 역순으로 돌림
    result = list(reversed(result))
    # 내 팀의 순위 찾기
    for i in range(len(result)):
        if result[i][0] == t:
            print(i + 1)
            break
