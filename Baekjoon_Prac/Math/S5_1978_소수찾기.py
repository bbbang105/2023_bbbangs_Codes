N = int(input())

num = list(map(int, input().split()))
count = 0

for x in num:
    if x == 1:
        pass
    elif x == 2:
        count += 1
    else:
        for i in range(2,x):
            if x % i == 0:
                break
            elif i == x-1:
                count += 1
                
print(count)
    