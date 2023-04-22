import sys
input = sys.stdin.readline

dp = [0] * 1001
dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
dp[5] = 21

n = int(input())
# x는 x-1값에 대해 2x1파일 하나만을 붙일 수 있으므로 그대로
# x-2값에 대해서는 1x2파일 2개 or 2x2를 붙일 수 있으므로 2를 곱해줌
for x in range(6,n+1):
    dp[x] = dp[x-1] + dp[x-2]*2

print(dp[n]%10007)
    