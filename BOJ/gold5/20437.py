# 문자열 게임 2
# 문자열, 슬라이딩 윈도우
import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    w = input().strip()
    k = int(input())
    alpha_dict = defaultdict(list)
    for idx, char in enumerate(w):
        if w.count(char) >= k:  # 해당 문자가 k개 이상이면
            alpha_dict[char].append(idx)  # ex) 'a' : [0, 4, 8]

    result = []
    for alpha, idx_list in alpha_dict.items():
        if len(idx_list) == k:  # 문자가 k개만큼 있으면
            # ex) k가 2일 때,  'a' : [0, 3]
            # 3-0+1가 연속 문자열의 길이
            size = idx_list[-1] - idx_list[0] + 1
            result.append(size)
        elif len(idx_list) > k:  # 문자 개수가 k보다 클 때
            # ex) 'a': [0, 4, 7]
            # -> 0~4/4~7인 경우
            idx = 0
            for i in range(idx + k - 1, len(idx_list)):
                size = idx_list[i] - idx_list[idx] + 1
                result.append(size)
                idx += 1

    # 연속 문자열을 길이 순 정렬
    result.sort()
    if not result:
        print(-1)
    else:
        print(result[0], result[-1])
