# 문자열 교환
# 브루트포스 알고리즘, 슬라이딩 윈도우
import sys

input = sys.stdin.readline

s = input().strip()

# aabbaabba에서 a가 연속일 때
# -> s에서 'a'의 개수만큼이 하나의 윈도우
# ex) aaaaabbbb

# 윈도우를 a의 연속으로 바꾸려면 윈도우 내의 b와 외부의 a를 교환
# -> 윈도우 내의 b의 개수가 최소인 경우가 답
# aabbaaabaaba -> a가 8개이므로 윈도우 사이즈는 8
# 1. [ a, a, b, b, a, a, a, b] => 교환 횟수: 3
# 2. [ a, b, b, a, a, a, b, a] => 교환 횟수: 3
# 3. [ b, b, a, a, a, b, a, a] => 교환 횟수: 3
# 4. [ b, a, a, a, b, a, a, b] => 교환 횟수: 3
# 5. [ a, a, a, b, a, a, b, a] => 교환 횟수: 2
# 6. [ a, a, b, a, a, b, a, a] => 교환 횟수: 2
# 7. [ a, b, a, a, b, a, a, a] => 교환 횟수: 2
# 8. [ b, a, a, b, a, a, a, b] => 교환 횟수: 3
cnt_a = s.count('a') # 윈도우 사이즈
l = 0
result = sys.maxsize

while l < len(s):
    r = l + cnt_a
    if r > len(s): # 원형이기 때문에 r이 s의 크기보다 커지는 경우 고려
        arr = s[l:len(s)] + s[:r - len(s)]
    else:
        arr = s[l:r]

    # 해당 윈도우에서 b의 개수만큼 교환해야 함
    result = min(result, arr.count('b'))
    l += 1

print(result)
