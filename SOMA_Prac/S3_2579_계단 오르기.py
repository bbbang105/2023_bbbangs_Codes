import sys
input = sys.stdin.readline
lst = []
dp = []

for _ in range(int(input())):
    lst.append(int(input()))
    
dp.append(lst[0]) # 첫 번째 계단에서의 최대값 저장
dp.append(max(lst[0]+lst[1], lst[1])) # 두 번째 계단에서의 최대값 저장
dp.append(max(lst[0]+lst[2], lst[1]+lst[2])) # 세 번째 계단에서의 최대값 저장

# 현재 위치가 4번째 계단일 때,
# 1) 2번째 계단까지의 최대값 + 현재 계단의 가중치
# 2) 1번째 계단까지의 최대값 + (현재 계단-1)의 가중치 + 현재 계단의 가중치
# 라는 2가지 경우만 나올 수 있기에, 두 수를 비교하여 넣어줌
for i in range(3,len(lst)):
    dp.append(max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i]))
    
print(dp.pop())