n2 = 'A,B,C'
n3 = 'D,E,F'
n4 = 'G,H,I'
n5 = 'J,K,L'
n6 = 'M,N,O'
n7 = 'P,Q,R,S'
n8 = 'T,U,V'
n9 = 'W,X,Y,Z'

cnt = 0
for i in input():
    if i in n2:
        cnt += 3
    elif i in n3:
        cnt += 4
    elif i in n4:
        cnt += 5
    elif i in n5:
        cnt += 6
    elif i in n6:
        cnt += 7
    elif i in n7:
        cnt += 8
    elif i in n8:
        cnt += 9
    elif i in n9:
        cnt += 10
        
print(cnt)