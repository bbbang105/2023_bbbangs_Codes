import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    word = input().rstrip()
    stk = []
    
    for i in range(len(word)): # 문자열의 길이만큼 반복
        if stk and stk[-1] == word[i]: # 짝이 맞으면 pop()
            stk.pop()
        else:                   # 아니면 append()
            stk.append(word[i])
            
    if not stk:                 # 모두 짝이 맞아 스택이 비면 +1
        cnt += 1
        
print(cnt)