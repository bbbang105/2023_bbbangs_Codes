from collections import deque
import sys
input = sys.stdin.readline

dq = deque() # 문자열을 담음
num = deque() # 버튼의 숫자를 담음

for _ in range(int(input())):
    c = input().split()
    
    if c[0] == '1':      # 1일시 오른쪽 삽입
        num.append(c[0])
        dq.append(c[1])
        
    elif c[0] == '2':    # 2일시 왼쪽 삽입
        num.append(c[0])
        dq.appendleft(c[1])
        
    elif c[0] == '3' and num: # 3이 처음에 나온 게 아닌 경우
        if num.pop() == '1':  # 직전의 버튼이 1이면
            dq.pop()          # 오른쪽에서 제거
        else:                 # 직전의 버튼이 2이면
            dq.popleft()      # 왼쪽에서 제거
    
if not dq:              # 데큐가 비어있으면
    print(0)            # 0출력
else:
    print(''.join(dq))  # join으로 문자열을 합쳐 출력