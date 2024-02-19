# 상어 초등학교
# 구현
import sys

input = sys.stdin.readline
n = int(input())
students = [list(map(int, input().split())) for _ in range(n ** 2)]
classroom = [[0] * n for _ in range(n)]

for num in range(n ** 2):
    # 좋아하는 학생의 번호
    like_std = students[num][1:]
    # 현재 학생이 앉을 수 있는 자리 리스트
    seat_list = []
    for r in range(n):
        for c in range(n):
            # 현재 칸에서
            if classroom[r][c] == 0:
                like_cnt, empty_cnt = 0, 0
                # 인접한 칸 탐색
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = r + dx, c + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생 수
                        if classroom[nx][ny] in like_std:
                            like_cnt += 1
                        # 비어있는 칸 수
                        if classroom[nx][ny] == 0:
                            empty_cnt += 1
                seat_list.append([like_cnt, empty_cnt, r, c])

    # 좋아하는 학생 수, 인접한 빈 칸 수, 행의 번호가 작게, 열의 번호가 작게 정렬
    seat_list.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]), reverse=True)
    classroom[seat_list[0][2]][seat_list[0][3]] = students[num][0]

result = 0
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
# 딕셔너리에 학생별 좋아하는 학생 번호를 저장
std = {}
for k in range(n * n):
    tmp = students[k]
    num, likes = tmp[0], tmp[1:]
    std[num] = likes

for r in range(n):
    for c in range(n):
        cnt = 0
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = r + dx, c + dy
            if 0 <= nx < n and 0 <= ny < n:
                if classroom[nx][ny] in std[classroom[r][c]]:
                    cnt += 1
        result += score[cnt]

print(result)
