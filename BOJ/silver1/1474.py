# 밑 줄
# 그리디 알고리즘, 문자열
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
words = []
size = 0
for _ in range(n):
    tmp = input().strip()
    words.append(tmp)
    size += len(tmp)

# 추가할 _의 개수
size = m - size
div, mod = divmod(size, n - 1)
arr = []
# 우선 단어 사이 _*div개가 들어가야함
# size에서 div만큼 차감
for i in range(1, n):
    arr.append("_" * div)
    size -= div

# 남은 _ 발생
# _가 소문자 보다 작으므로 우선 단어가 소문자로 시작하는 단어 앞에 추가
# 추가한 만큼 차감
for i in range(1, n):
    if size > 0 and words[i][0].islower():
        arr[i - 1] += "_"
        size -= 1

# 아직 남았으면 대문자로 시작하는 단어에 추가
for i in range(n - 1, 0, -1):
    if size > 0 and words[i][0].isupper():
        arr[i - 1] += "_"
        size -= 1

result = words[0]
for i in range(1, n):
    result += arr[i - 1]
    result += words[i]

print(result)
