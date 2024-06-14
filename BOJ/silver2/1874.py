# 스택 수열
# 자료 구조, 스택
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
st = []
num = 1
result = []
flag = True


for i in range(n):
    while num <= arr[i]:
        st.append(num)
        num += 1
        result.append("+")

    if st[-1] == arr[i]:
        st.pop()
        result.append("-")
    else:
        print("NO")
        break
else:
    for i in result:
        print(i)
