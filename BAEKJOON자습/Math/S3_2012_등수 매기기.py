import sys
input = sys.stdin.readline
lst = []

for _ in range(int(input())):
    lst.append(int(input()))
    
lst.sort()

grade = 1
sum = 0
for i in lst:
    sum += abs(i-grade)
    grade += 1
    
print(sum)