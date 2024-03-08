# 옥상 정원 꾸미기
# 자료 구조, 스택
import sys

input = sys.stdin.readline
buildings = []
n = int(input())
for i in range(n):
    buildings.append(int(input()))

st = []
result = 0

for i in range(n):
    # 현재 탐색중인 빌딩의 크기가 스택에 있는 빌딩 크기보다 크면
    # 스택에 있는 빌딩은 현재 탐색 중인 빌딩 못봄
    # pop연산
    while st and st[-1] <= buildings[i]:
        st.pop()

    # 현재 탐색 중인 빌딩
    st.append(buildings[i])
    # 스택에 있는 빌딩은 스택 0번째 빌딩이
    # 볼 수 있는 빌딩
    result += len(st) - 1
    print(st)

print(result)
