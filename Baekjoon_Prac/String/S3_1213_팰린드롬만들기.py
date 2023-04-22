from collections import Counter # Counter 메소드 사용

word = input()
word = sorted(word) # 정렬
check = Counter(word) # 개수 파악을 위함

cnt = 0 # 홀수 개수
center = '' # 홀수 문자열

for i in check:
    if check[i] % 2 != 0:
        cnt += 1
        center += i 
        word.remove(i) # 모두 짝수로 맞추기 위해, 홀수 문자열 하나를 제거
        
    if cnt > 1: # 홀수의 개수가 1보다 큰 경우, 팰린드롬이 되지 못 함
        break
    
if cnt > 1: # 홀수의 개수가 1보다 큰 경우, 팰린드롬이 되지 못 함
    print('I\'m Sorry Hansoo')
    
else: # 팰린드롬으로 만들 수 있는 경우
    res = '' # 가운데를 기준으로 반쪽을 만듦
    for i in range(0,len(word),2): # 짝수 개수인 문자열만 있기에, 한 칸씩 띄워서 넣어줌
        res += word[i]
        
    print(res + center + res[::-1]) # 반쪽 + 홀수 문자열(있다면) + 반쪽(reverse)
