price,quantity,money = map(int,input().split())

if money > price*quantity:
    print(0)
else:
    print(price*quantity - money)