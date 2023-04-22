import sys
input = sys.stdin.readline

S = input()
for i in range(97,123): # 영어 소문자 아스키 코드 97~122
    alphabet = chr(i) # 문자로 변환
    if alphabet in S: # S에 들어 있는 알파벳이면,
        print(S.index(alphabet), end = ' ') # 인덱스 출력
    else:
        print(-1, end = ' ')
