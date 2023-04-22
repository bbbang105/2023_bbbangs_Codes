from collections import deque # deque 메소드 선언

n,k = map(int,input().split())

all = deque()
for i in range(1,n+1): # 초기 인원 구성
    all.append(i)

answer = [] # 제거한 인원의 인덱스
while all: # 사람이 남아 있을 때 까지
    for j in range(k-1): # 제거할 인원 전까지 뽑아 다시 뒤로 추가
        all.append(all.popleft())
    answer.append(all.popleft()) # 제거

print(str(answer).replace('[','<').replace(']','>')) # list를 str로 형변환한 뒤, replace를 이용