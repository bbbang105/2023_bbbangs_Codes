while(True):
    men,women = map(int, input().split())
    if men == 0 and women == 0:
        break
    else:
        print(men+women)