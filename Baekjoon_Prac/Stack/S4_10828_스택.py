import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    a = input().split()

    # push
    if a[0] == 'push':
        stack.append(a[1])
    # pop
    elif a[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # size
    elif a[0] == 'size':
        print(len(stack))
    # empty
    elif a[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # top
    elif a[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        