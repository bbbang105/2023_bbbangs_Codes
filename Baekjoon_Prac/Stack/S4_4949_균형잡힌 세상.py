while(True):
    s = input()
    
    if s == '.': # 온점만 나올 시, 종료
        break
    
    stk = []
    temp = True 
    for i in s:
        if i == '(' or i == '[': # 여는 소괄호 & 대괄호가 나올 시, 스택에 추가
            stk.append(i)
            
        elif i == ')': # 닫는 소괄호가 나올 시,
            if not stk or stk[-1] == '[': # 스택이 비었거나, 대괄호가 마지막에 있으면
                temp = False # 균형X 
                break
            elif stk[-1] == '(': # 짝이 맞을 시, 마지막 제거
                stk.pop()
                
        elif i == ']': # 닫는 대괄호가 나올 시,
            if not stk or stk[-1] == '(': # 스택이 비었거나, 소괄호가 마지막에 있으면
                temp = False # 균형X 
                break
            elif stk[-1] == '[': # 짝이 맞을 시, 마지막 제거
                stk.pop()
                
    if temp == True and not stk: # 모든 짝이 맞을 경우
        print('yes')
    else:
        print('no')