# 전화번호 목록
# 자료구조, 문자열, 정렬, 트리, 트라이
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    phone = [input().strip() for _ in range(n)]
    # 한 번호가 다른 번호의 접두어인 경우 파악을 위해 사전순 정렬
    phone.sort()
    # 현재 번호가 다음 번호의 접두어인 경우 확인
    for i in range(n - 1):
        size = len(phone[i])
        if phone[i] == phone[i + 1][:size]:
            print("NO")
            break
    else:
        print("YES")
