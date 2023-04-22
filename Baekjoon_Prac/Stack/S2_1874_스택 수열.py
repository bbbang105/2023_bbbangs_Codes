cnt = 0
stk = []
result = []
temp = True
    
for i in range(int(input())):
    num = int(input())
    
    while cnt < num: # 입력한 숫자만큼 넣기
        cnt += 1
        stk.append(cnt)
        result.append('+')

    if stk[-1] == num: # 같은 숫자가 되면 꺼내주기
           stk.pop()
           result.append('-')
           
    else:
        temp = False
        break # 에러 없이 종료
        
if temp == False:
    print('NO')
else:
    print('\n'.join(result)) # 줄 바꿈으로 출력