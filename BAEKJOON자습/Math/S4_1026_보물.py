T = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
A = sorted(A)
B = sorted(B)
B.reverse()

result = 0
for i in range(T):
    result += A[i] * B[i]
    
print(result)


