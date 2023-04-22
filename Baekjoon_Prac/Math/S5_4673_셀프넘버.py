numbers = list(range(1,10001)) # 1 ~ 10,000까지 숫자가 담긴 리스트 생성

remove_lst = [] # 생성자가 있는 숫자를 담을 리스트 생성

for num in numbers:
    for i in str(num): # 각 자리수를 더하기 위해 str로 형변환
        num += int(i) # 생성자가 있는 숫자
    if num <= 10000:
        remove_lst.append(num)
        
for remove_num in set(remove_lst): # set으로 중복 제거
    numbers.remove(remove_num) # self number만을 남기고 제거함
    
for selfnum in numbers:
    print(selfnum)