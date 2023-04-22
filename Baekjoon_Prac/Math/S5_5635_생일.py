lst = []
for _ in range(int(input())):
    n,d,m,y = input().split()
    lst.append([n,int(d),int(m),int(y)])

lst.sort(key = lambda x : (x[3],x[2],x[1])) # 람다 함수 활용하여 정렬

print(lst[-1][0]) # 가장 나이가 적은 사람 (맨 뒤)
print(lst[0][0]) # 가장 나이가 많은 사람 (맨 앞)
    
    
    