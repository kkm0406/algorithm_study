# 다음 순열
# 수학, 조합론
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 예시: 136541
# 1. 끝에서부터 비교해 앞에것이 더 작은 곳을 i로 정한다. (3 < 6)
# 2. 끝에서부터 i값보다 큰 값을 찾아 j로 정한다. (3 < 4)
# 3. i값과 j값을 서로 바꾼다.
# 4. i뒤에 있는 것들을 순서를 뒤집어준다.
# 답: 141356


# l을 -1로 설정하고 s[i] < s[i+1]을 만족하는 최대 i를 찾아 l에 저장
# l이 -1이라면 모든 문자가 오름차순 정렬 -> 마지막 단어
l = -1
for i in range(n - 1):
    if arr[i] < arr[i + 1]:
        l = i

if l == -1:
    print(-1)
    exit()

# 뒤에서부터 탐색하면서 s[l]보다 큰 문자를 찾음
# s[i] > s[l]를 만족하는 i를 r에 저장하고 break
for i in range(n - 1, -1, -1):
    if arr[l] < arr[i]:
        r = i
        break

# 두 문자의 위치를 바꿈
arr[l], arr[r] = arr[r], arr[l]
# l+1번째부터 뒤의 문자들은 역순으로 돌림
result = arr[:l + 1] + list(reversed(arr[l + 1:]))

print(*result)
