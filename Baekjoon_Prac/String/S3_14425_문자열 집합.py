import sys
input = sys.stdin.readline

N = list(map(int, input().split()))

stk = []

for _ in range(N[0]):
    stk.append(input().rstrip())
    
stk = set(stk)

cnt = 0
for _ in range(N[1]):
    if input().rstrip() in stk:
        cnt += 1
        
print(cnt)