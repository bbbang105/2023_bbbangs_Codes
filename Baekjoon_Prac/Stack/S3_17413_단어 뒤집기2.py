import sys
input = sys.stdin.readline

new = '' # 새로운 문자열
stk = [] # 뒤집어서 출력할 문자열을 저장
c = 0 # index
word = input()

while(True):
    if word[c] == '<':
        while(word[c] != '>'): # 닫는 괄호가 나올 때까지
            new += word[c]
            c += 1
            
    elif word[c] == '>': # 닫는 괄호가 나오면
        new += '>'
        c += 1
        
    elif word[c].isalnum(): # 괄호에 포함되지 않은 문자열일 때
        while(word[c].isalnum()): # 공백이 나오기 전까지
            stk.append(word[c])
            c += 1
        new += ''.join(stk[::-1]) # 뒤집어서 추가
        stk = [] # 스택 초기화
        
    else: # 공백일 때
        new += ' '
        c += 1
    
    if len(new) == len(word): # 새로운 문자열 생성 완료
        break
    
print(new)