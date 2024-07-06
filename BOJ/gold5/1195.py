# 킥다운
# 구현, 브루트포스 알고리즘
import sys

input = sys.stdin.readline
top = input().strip()
bottom = input().strip()
len_bottom, len_top = len(bottom), len(top)
result = len(top) + len(bottom)


# bottom 한 칸씩 옆으로 이동하면서 맞물리는 지 확인
# -2 -1 0 1 2 3
#  0  0 2 1 1 2
#  2  2 1
for idx in range(-len_bottom + 1, len_top):
    flag = True  # 맞물리는 지 확인하는 변수
    # bottom이 이동하는 모든 가능한 위치 탐색
    for i in range(len_bottom):
        if 0 <= idx + i < len_top:
            # 맞물리지 않는 경우 -> 그 위치는 불가
            if top[idx + i] == "2" and bottom[i] == "2":
                flag = False
                break

    if flag:
        # top에 완전히 포개지거나 옆으로 삐져나온 경우
        if idx >= 0:
            current_width = max(len_top, len_bottom + idx)
        # botto에 완전히 포개지거나 옆으로 삐져나온 경우
        else:
            current_width = max(len_bottom, len_top - idx)

        result = min(result, current_width)

print(result)
