cnt = 0 # 그룹단어 개수

for _ in range(int(input())):
    word = input()
    lst = [] 
    flag = True
    
    for i in word:
        if i not in lst: # 처음 나오는 알파벳이면
            lst.append(i) # 리스트에 추가
        elif i in lst: # 중복된 알파벳일 때,
            if i != lst[-1]: # 연속된 것이 아니면
                flag = False # False
                break
            else:
                pass
    
    if flag: 
        cnt += 1
        
print(cnt)