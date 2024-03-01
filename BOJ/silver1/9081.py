# 단어 맞추기
# 수학, 구현, 문자열, 조합론
import sys

input = sys.stdin.readline

# 예시: 136541
# 1. 끝에서부터 비교해 앞에것이 더 작은 곳을 i로 정한다. (3 < 6)
# 2. 끝에서부터 i값보다 큰 값을 찾아 j로 정한다. (3 < 4)
# 3. i값과 j값을 서로 바꾼다.
# 4. i뒤에 있는 것들을 순서를 뒤집어준다.
# 답: 141356

for _ in range(int(input())):
    s = list(input().strip())

    # l을 -1로 설정하고 s[i] < s[i+1]을 만족하는 최대 i를 찾아 l에 저장
    # l이 -1이라면 모든 문자가 오름차순 정렬 -> 마지막 단어
    l = -1
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            l = i

    if l == -1:
        print("".join(s))
        continue

    # 뒤에서부터 탐색하면서 s[l]보다 큰 문자를 찾음
    # s[i] > s[l]를 만족하는 i를 r에 저장하고 break
    for i in range(len(s)-1, -1, -1):
        if s[l] < s[i]:
            r = i
            break

    # 두 문자의 위치를 바꿈
    s[l], s[r] = s[r], s[l]
    # l+1번째부터 뒤의 문자들은 역순으로 돌림
    result = s[:l+1] + list(reversed(s[l+1:]))
    print("".join(result))
