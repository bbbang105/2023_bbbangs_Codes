import sys
input = sys.stdin.readline

opn = [] # 피연산자 스택
stk = [] # 계산 스택
N = int(input()) # 피연산자의 개수
exp = input().rstrip() # 후위 표기식

for _ in range(N):
    opn.append(int(input())) # 피연산자 할당

for x in exp: # 후위 계산 과정
    if 'A' <= x <= 'Z':
        stk.append(opn[ord(x) - ord('A')]) # 알파벳 순서대로 할당되기 때문 (Ex. A면 opn[0])
    else: 
        n2 = stk.pop() # 순서 맞추기
        n1 = stk.pop()
        
        if x == '+':
            stk.append(n1 + n2)
        elif x == '-':
            stk.append(n1 - n2)
        elif x == '*':
            stk.append(n1 * n2)
        else:
            stk.append(n1 / n2)
            
print('%.2f'% stk[0])
