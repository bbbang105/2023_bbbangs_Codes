import sys
sys.stdin.readline

N = int(input())
num = input()
num_sum = 0

for i in num:
    num_sum += int(i)
    
print(num_sum)