T = int(input()) # 구성할 팀의 개수

level = list(map(int,input().split())) # 개인의 역량

lst = [] # 팀의 역량 합산

while(len(level)>0):
    a = max(level)
    b = min(level)
    lst.append(a+b)
    level.remove(a)
    level.remove(b)
    
print(min(lst))