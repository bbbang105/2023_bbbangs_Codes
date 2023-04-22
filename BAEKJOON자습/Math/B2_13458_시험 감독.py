T = int(input())

num_lst = list(map(int,input().split()))

main, sub = map(int, input().split())

count = 0
for i in num_lst:
    i -= main
    count += 1
    if i % sub == 0:
        count += i // sub
    else:
        count += i // sub + 1
        
print(count)
