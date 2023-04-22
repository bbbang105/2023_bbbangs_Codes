import sys
input = sys.stdin.readline

stk = [] # 짝을 맞추기 위한 공간
brck = input().rstrip() # 오른쪽 공백 제거

for i in brck:
    if i == '(': # 여는 괄호일 시
        stk.append(i)
    elif i == ')' and stk: # 닫는 괄호일 시 스택 확인하여 짝 맞춤
        if stk[-1] == '(':
            stk.pop()
        else:
            stk.append(i)
    elif i == ')' and not stk: # 닫는 괄호일 시 스택이 비어있으면
        stk.append(i)
            
print(len(stk))