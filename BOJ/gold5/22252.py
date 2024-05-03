# 정보 상인 호석
# 자료 구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 우선순위 큐
import heapq
import sys

input = sys.stdin.readline

q = int(input())
value = 0
g = {}
for i in range(q):
    tmp = input().split()
    num, name, k, c = int(tmp[0]), tmp[1], int(tmp[2]), tmp[3:]
    if num == 1:  # 딕셔너리에 데이터 추가
        # 이름 없으면
        if name not in g:
            # 우선순위큐에 넣어서
            q = []
            for val in c:
                heapq.heappush(q, -int(val))
            # 딕셔너리 추가
            g[name] = q
        else:
            # 기존의 딕셔너리에 우선순위 고려해 push
            for val in c:
                heapq.heappush(g[name], -int(val))
    else:
        if name in g:
            # 하나씩 pop하면서 가치를 더함
            for j in range(k):
                if g[name]:
                    val = -1 * heapq.heappop(g[name])
                    value += val
                # pop할 값이 없으면 바로 반복문 종료
                else:
                    break
        else:
            continue

print(value)
