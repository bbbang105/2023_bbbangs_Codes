A = int(input())
B= int(input())
C = int(input())

pro = A*B*C

pro = list(str(pro))

for i in range(0,10):
    print(pro.count(str(i)))