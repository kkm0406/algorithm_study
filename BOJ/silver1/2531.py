# 회전 초밥

import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
# 회전초밥 고려
# 길이가 10인 벨트에서 9, 10, 1, 2, ...과 같은 순서로 고를 때를 고려
# k-2번째 원소까지 이어붙임
sushi += sushi[:k - 1]
l, r = 0, k - 1
result = 0
pick = {}
# 맨 처음 고를 때
for i in range(l, r + 1):
    if sushi[i] not in pick:
        pick[sushi[i]] = 1
    else:
        pick[sushi[i]] += 1

if c not in pick:
    # 쿠폰 초밥을 추가로
    result = len(pick) + 1
else:
    result = len(pick)

while r < len(sushi):
    prev = sushi[l]
    # 한 칸 씩 오른쪽 이동
    l += 1
    r += 1
    # 이전 고른 초밥 중 가장 처음 고른 초밥 개수 -1
    pick[prev] -= 1
    # 해당 초밥의 개수가 0 -> 벨트에 없는 경우 -> 삭제
    if pick[prev] == 0:
        del pick[prev]

    # 새로운 초밥을 고름
    if r < len(sushi):
        if sushi[r] in pick:
            pick[sushi[r]] += 1
        else:
            pick[sushi[r]] = 1

    # 쿠폰 초밥 고려
    if c not in pick:
        cnt = len(pick) + 1
    else:
        cnt = len(pick)

    if cnt > result:
        result = cnt

print(result)
