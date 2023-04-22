# 스택으로 다시 해보기 (4/17)
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque(map(int, input().split()))

c = 0
while(c < len(dq)-1):           # 마지막 값만 남겨두고 반복
    if dq[c] == max(dq):        # 가장 큰 값이면 무조건 -1
        dq[c] = -1
        c += 1
    else:                       # 아니면 오른쪽의 숫자들과 비교 작업
        m = dq[c]               # m = 현재의 숫자
        c += 1
        c2 = c                  # 반복 비교를 위한 새로운 인덱스 생성
        while(True):
            if m >= dq[c2]:     # 본인보다 큰 값이 아니면 continue
                c2 += 1
                continue
            else:               # 큰 값을 찾으면 바꿔주고 break
                dq[c-1] = dq[c2]
                break     
            
dq[-1] = -1 # 마지막 값은 무조건 -1 이므로

print(*dq)  # 리스트 요소 한 번에 출력