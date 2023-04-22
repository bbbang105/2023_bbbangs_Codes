import sys
input = sys.stdin.readline

for i in range(int(input())):
    word = input()
    new = word.split()
    print('Case #' + str(i+1) + ': ' + ' '.join(new[::-1]))