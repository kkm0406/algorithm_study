# 탑
# 자료 구조, 스택
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# 레이저 신호를 수신하는 탑
towel = [0] * n
# 탑의 인덱스와 높이를 저장하는 스택
st = []

# 왼쪽 방향으로 발사하기 때문에 역순으로 탐색
for i in range(n - 1, -1, -1):
    if not st:
        st.append([i, arr[i]])
    else:
        while st:
            # 인덱스와 높이
            idx, prev = st[-1]
            # 스택에 저장된 높이보다 현재 탑의 높이가 크면
            if prev < arr[i]:
                # idx번째 탑에 현재 탑의 번호 저장
                towel[idx] = i + 1
                # 스택 pop
                st.pop()
            else:
                break
        # 현재 탐색 중인 탑의 정보 append
        st.append([i, arr[i]])

print(*towel)
