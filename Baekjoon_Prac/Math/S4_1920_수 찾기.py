import sys
input = sys.stdin.readline

T1 = int(input())
N1 = set(input().split()) # 중복 값 제거를 위해 set 사용
T2 = int(input())
N2 = input().split()

for i in N2:
    if i in N1:
        print(1)
    else:
        print(0)