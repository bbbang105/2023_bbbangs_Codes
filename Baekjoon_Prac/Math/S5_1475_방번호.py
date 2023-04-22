from collections import Counter

n = input()

check = Counter(n)
cnt = 1

for i in check:
    # 숫자가 6 또는 9인 경우
    if i in '6,9':
        check[i] = (check[i]+1)//2 # 홀수 개수임을 방지해 1을 더해주고 2로 나눔
    cnt = max(cnt,check[i]) # 가장 큰 값으로 할당
    
print(cnt)

