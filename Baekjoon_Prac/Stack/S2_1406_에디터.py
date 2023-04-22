import sys
input = sys.stdin.readline

stk = []
word = list(input().rstrip()) # rstrip() 사용으로 오른쪽 공백 제거

for i in range(int(input())):
    cmd = input().split() # 입력받은 명령어
    
    if cmd[0] == 'L' and word: # 커서가 문장의 맨 앞(=단어가 비면)이면 무시
        stk.append(word.pop())
    elif cmd[0] == 'D' and stk: # 커서가 문장의 맨 뒤(=스택이 비면)이면 무시
        word.append(stk.pop())
    elif cmd[0] == 'B' and word: # 커서가 문장의 맨 앞(=단어가 비면)이면 무시
        word.pop()
    elif cmd[0] == 'P': # P명령어
        word.append(cmd[1])
        
word.extend(reversed(stk))
print(''.join(word))