n = int(input())

lst = list(map(int, input().split()))

lst.sort()

per_time = 0
all_time = 0

for i in lst:
    per_time += i
    all_time += per_time
    
print(all_time)