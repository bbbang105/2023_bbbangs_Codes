num = 0
lst = []

for i in range(4):
    a,b = map(int,input().split())
    if i == 0:
        num += b
        lst.append(num)
    else:
        num = num-a+b
        lst.append(num)
    
print(max(lst))