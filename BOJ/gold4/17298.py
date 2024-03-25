# 오큰수
# 자료 구조, 스택
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
st = []  # 인덱스를 저장할 스택
result = [-1] * n
for i in range(n):
    # i번쨰 원소가 스택 인덱스의 원소보다 클때
    while st and arr[st[-1]] < arr[i]:
        # 해당인덱스에 오큰수 저장
        result[st.pop()] = arr[i]
    st.append(i)

print(*result)
