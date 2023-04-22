import sys
input = sys.stdin.readline

stk = []
cnt = 1 # 비교하는 대상인 본인은 무조건 보이게 되니 포함

for i in range(int(input())):
    stk.append(int(input())) # 스택에 입력값을 다 넣어줌
    
max = 0
for x in stk[-2::-1]: # 본인을 제외하고 역순으로
    if x > stk[-1] and x > max: # 비교
        max = x
        cnt += 1
        
print(cnt)