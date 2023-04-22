stack = []

for _ in range(int(input())):
    x = int(input())
    if x != 0:
        stack.append(x)
    else:
        stack.pop()
        
print(sum(stack))