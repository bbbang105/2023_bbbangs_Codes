import sys
input = sys.stdin.readline

N = int(input())

if N < 100:
    cnt = N
    print(cnt)
else:
    cnt = 99 # 100 이전의 모든 숫자는 한수임
    for i in range(100,N+1):
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            cnt += 1
    
    print(cnt)
        