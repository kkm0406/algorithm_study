# 연산자 끼워넣기
# 브루트포스 알고리즘, 백트래킹

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
mark = list(map(int, input().split()))
ops = ("+", "-", "*", "/")
arr = []
result = []


def dfs(depth):
    if depth == n - 1:
        num = a[0]
        for i in range(len(arr)):
            if arr[i] == "+":
                num += a[i + 1]
            elif arr[i] == "-":
                num -= a[i + 1]
            elif arr[i] == "*":
                num *= a[i + 1]
            else:
                if num < 0 and a[i + 1] > 0:
                    num = (-1 * num) // a[i + 1]
                    num = -num
                else:
                    num //= a[i + 1]
        result.append(num)
    else:
        for i in range(4):
            if mark[i] > 0:
                mark[i] -= 1
                arr.append(ops[i])
                dfs(depth + 1)
                arr.pop()
                mark[i] += 1


dfs(0)
print(int(max(result)))
print(int(min(result)))
