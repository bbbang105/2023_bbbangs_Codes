import sys
input = sys.stdin.readline

bracket = list(input().rstrip())

stack = []
answer = 0 # 결과값
tmp = 1 # 현재 괄호의 가중치

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2 # 가중치 * 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3 # 가중치 * 3

    elif bracket[i] == ")": # 닫는 소괄호가 나올 경우
        if not stack or stack[-1] == "[": # 짝이 안 맞는 경우
            answer = 0 # 초기화
            break
        if bracket[i-1] == "(": # 짝이 맞는 경우
            answer += tmp # 현재 가중치 만큼 +
        stack.pop() 
        tmp //= 2 # 사용한 가중치 만큼 //

    else:                   # 닫는 대괄호가 나올 경우
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)