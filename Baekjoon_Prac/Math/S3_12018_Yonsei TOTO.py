import sys
input = sys.stdin.readline
T,mile = map(int,input().split())

cnt = 0
pos = []
for _ in range(T):
    app,TO = map(int,input().split())
    lst = list(map(int, input().split()))
    
    if TO>app:
        pos.append(1)
    else:
        lst.sort(reverse = True)
        pos.append(lst[TO-1])
    
for i in sorted(pos):
    if mile >= i:
        cnt += 1
        mile -= i
        
print(cnt)