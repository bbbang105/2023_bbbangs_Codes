import sys
input = sys.stdin.readline

lst = []
for _ in range(9): # 아홉 난쟁이의 값 저장
    lst.append(int(input()))
    
for i in range(9): # 완전탐색법 사용
    for j in range(9):
        if sum(lst) - lst[i] - lst[j] == 100:
            n1 = lst[i] # 일곱 난쟁이가 아닌 두 난쟁이
            n2 = lst[j]
            break
        
lst.remove(n1) # 값을 제거해줌
lst.remove(n2)

for x in sorted(lst): # 오름차순 정렬
    print(x)