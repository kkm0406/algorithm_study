# ZOAC
# 구현, 문자열, 재귀
import sys

input = sys.stdin.readline
s = list(input().strip())
result = [""] * len(s)

# 글자를 완성할 떄마다 사전 순서가 최소 -> 처음 사전순으로 가장 작은 것 기준으로 오른쪽 완성 후 왼쪽 완성
# 이분법적 접근 + 재귀
def dfs(start, s):
    # 더 이상 배열이 존재하지 않으면 종료
    if not s:
        return
    min_val = min(s)
    # 배열에서 최솟값의 위치
    min_idx = s.index(min_val)
    result[start + min_idx] = min_val
    print("".join(result))
    # 가장 작은 거 기준 오른쪽부터 재귀해야 사전순으로 가장 작은 값
    dfs(start + min_idx + 1, s[min_idx + 1:])
    dfs(start, s[:min_idx])


dfs(0, s)
