import sys
input = sys.stdin.readline

df = [0]*91 # df 생성
# 알아낸 값 저장
df[1] = 1
df[2] = 1
df[3] = 2
df[4] = 3
df[5] = 5

N = int(input())

for x in range(6,N+1):
    df[x] = df[x-2] + df[x-1]
    
print(df[N])