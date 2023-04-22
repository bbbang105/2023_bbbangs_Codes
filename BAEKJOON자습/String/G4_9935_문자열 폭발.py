import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()

stk = []                # 새로운 문자열을 담음

for i in word:
    stk.append(i)       
    if ''.join(stk[-len(bomb):]) == bomb: # bomb와 동일한 길이만큼만 비교
        del stk[-len(bomb):]              # 동일할 시, 그만큼 제거
        
ans = ''.join(stk)

if ans:
    print(ans)
else:
    print('FRULA')