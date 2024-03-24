# 한 줄로 서기
# 구현

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
heights = []

for i in range(n - 1, -1, -1):
    if not heights:
        heights.append(i + 1)
    else:
        cnt = 0
        # 줄 선 사람들 탐색
        for j in range(len(heights)):
            # 자기보다 큰 사람 몇 명있는지 카운트
            if heights[j] > i + 1:
                cnt += 1
                # 기록과 동일할 때
                if cnt == arr[i]:
                    # 해당 위치에 선다
                    heights.insert(j + 1, i + 1)
                    break
        # 왼쪽에 큰 사람이 없는 경우
        else:
            heights.insert(0, i + 1)

print(*heights)
