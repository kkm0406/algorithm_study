# 평범한 배낭
# 다이나믹 프로그래밍, 배낭 문제
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

wv = [[0, 0]]
for _ in range(n):
    wv.append(list(map(int, input().split())))

# dp[n][k]: n번째 물건까지 중 무게가 k인 배낭의 최대 가치
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k+1):
        w = wv[i][0]
        v = wv[i][1]
        # 배낭의 허용 무게보다 물건의 무게가 더 크면 넣지 않음
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            # 현재 넣을 물건의 무게만큼 배낭에서 빼고 현재 물건을 넣는 겨 ㅇ우
            # 현재 물건을 넣지않고 이전 배낭 그대로 가는 경우
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])

print(dp[n][k])
