from collections import deque
import sys
input = sys.stdin.readline

n = int(input())    # 컴퓨터 개수
v = int(input())    # 연결선 개수
graph = [[] for i in range(n+1)] # 컴퓨터 개수만큼 그래프 초기화
visited = [0]*(n+1) # 방문한 컴퓨터인지 (0,1)로 표시

for _ in range(v):  # 그래프 생성
    a,b = map(int,input().split())
    graph[a] += [b] 
    graph[b] += [a] # 양방향으로 연결
    
visited[1] = 1      # 1번 컴퓨터는 무조건 방문
Q = deque([1])      # 1번 컴퓨터부터 탐색 시작

while Q:                    # BFS
    cn = Q.popleft()        # 탐색할 컴퓨터의 번호
    for x in graph[cn]:
        if visited[x] == 0: # 아직 감염되지 않은 컴퓨터일 경우
            Q.append(x)    # 탐색할 리스트 추가 
            visited[x] = 1 # 감염(방문) 표시
            
print(sum(visited)-1)       # 1번 컴퓨터를 제외하고 합산