import sys
input = sys.stdin.readline

def factorial(x):
    num = 1
    for i in range(1,x+1):
        num *= i
    return num

print(factorial(int(input())))