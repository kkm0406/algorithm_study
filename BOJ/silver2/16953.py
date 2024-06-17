# A -> B
# 그래프 이론, 그리디 알고리즘, 그래프 탐색, 너비 우선 탐색
import sys

input = sys.stdin.readline

a, b = input().split()
cnt = 1
# b->a로 가면서 확인
while True:
    # 마지막 자릿수가 홀수인데 1이 아닌경우는 b->a 불가
    if int(b[-1]) % 2 == 1 and b[-1] != "1":
        print(-1)
        break

    # 1로 끝나면 마지막 자리수 제거
    if b[-1] == "1":
        b = b[:-1]
    # 아니면 /2
    else:
        b = str(int(b) // 2)
    cnt += 1

    if b == a:
        print(cnt)
        break

    # b가 a보다 작아니면 b->a 불가
    if int(b) < int(a):
        print(-1)
        break
