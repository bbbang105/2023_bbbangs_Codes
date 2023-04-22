n = int(input())

for i in range(n): # 테스트 케이스
    p = int(input())
    num = [] # 리스트 2개 생성
    men = []
    for x in range(p): # 입력 받을 선수 숫자
        a,b = map(str ,input().split()) 
        a = int(a)
        num.append(a)
        men.append(b)
    print(men[num.index(max(num))]) # num 리스트에서 가장 큰 숫자가 있는 인덱스를 찾은 후, men에서 꺼냄