import sys
input = sys.stdin.readline

df = [0]*1001 # df 생성
# 알아낸 값 저장
df[1] = 1
df[2] = 2
df[3] = 3
df[4] = 5
df[5] = 8

N = int(input())

for x in range(6,N+1):
    df[x] = df[x-2] + df[x-1]
    
print(df[N]%10007)
