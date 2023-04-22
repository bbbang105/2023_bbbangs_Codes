m,d = map(int,input().split())
cnt = 0 

if m == 1:
    cnt = d-1
else:
    for i in range(1,m): # m-1까지
        if i == 2: # 2월
            cnt += 28
        elif i in (4,6,9,11): # 30일까지 있는 달
            cnt += 30
        else: # 31일까지 있는 달
            cnt += 31
    cnt += d-1 # 남은 일수 더해줌
   
# 요일 계산 
if cnt % 7 == 0:
    print('MON')
elif cnt % 7 == 1:
    print('TUE')
elif cnt % 7 == 2:
    print('WED')
elif cnt % 7 == 3:
    print('THU')
elif cnt % 7 == 4:
    print('FRI')
elif cnt % 7 == 5:
    print('SAT')
else:
    print('SUN')