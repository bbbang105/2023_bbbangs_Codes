import sys
input = sys.stdin.readline

exp = input().split('-') # -를 기준으로 나누어 줌 (괄호)

num = []

for i in exp:
    sum = 0
    for j in i.split('+'):
        sum += int(j)
    num.append(sum)
    
n = num[0]

for x in range(1, len(num)):
    n -= num[x]
    
print(n)