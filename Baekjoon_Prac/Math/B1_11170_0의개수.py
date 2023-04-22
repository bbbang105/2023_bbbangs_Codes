for _ in range(int(input())):
    n,m = map(int,input().split())
    count = 0
    for i in range(n,m+1):
        i = str(i)
        for j in i:
            if j == '0':
                count += 1
    print(count)