# 0 만들기
# 구현, 문자열, 브루트포스 알고리즘, 백트래킹
import sys
from itertools import product

input = sys.stdin.readline
ops = ["+", "-", " "]

for _ in range(int(input())):
    n = int(input())
    nums = [i for i in range(1, n + 1)]
    # 중복 순역
    datas = list(product(ops, repeat=n - 1))
    answer = []
    for data in datas:
        result = ""
        for i in range(n - 1):
            result += str(nums[i]) + data[i]
        result += str(nums[-1])
        # eval 함수 사용을 위해 문자열 변환
        string = result.replace(" ", "")
        if eval(string) == 0:
            answer.append(result)

    answer.sort()
    for i in answer:
        print(i)
    print()
