a,b = map(int, input().split())

def gcd(a,b): # 최대공약수: 유클리드 호제법 사용
    while(b>0):
       a,b = b,a%b
    return a
   
def lcm(a,b): # 최소공배수 == 두 수의 곱 // 최대공약수
    return a * b // gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))