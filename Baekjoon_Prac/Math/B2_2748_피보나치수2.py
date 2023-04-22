fibo = [] # 리스트 생성

n = int(input())
num = 0

for i in range(n+1): # 0부터 n까지 리스트에 넣어서 계산함
    if i == 0: 
        num = 0 # n이 0일땐 0
    elif i <= 2:
        num = 1 # n이 1,2일땐 1
    else:
        num = fibo[-1] + fibo[-2] # n-1과 n-2의 합을 구해서 넣어줌
    fibo.append(num)
        
print(fibo[-1]) # 마지막 숫자(n)를 출력
        
    