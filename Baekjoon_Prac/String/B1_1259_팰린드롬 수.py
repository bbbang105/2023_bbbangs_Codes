import sys
input = sys.stdin.readline

while(True):
    x = input().rstrip()
    if x == '0':
        break
    elif x == x[::-1]:
        print('yes')
    else:
        print('no')