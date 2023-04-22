asc = [1,2,3,4,5,6,7,8]

X = list(map(int,input().split()))

if X == asc:
    print('ascending')
elif X == asc[::-1]:
    print('descending')
else:
    print('mixed')