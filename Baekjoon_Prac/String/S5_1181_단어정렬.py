lst = []

for _ in range(int(input())):
    lst.append(input())
    
lst = list(set(lst)) # 중복 제거
lst.sort() # 기본 정렬
lst.sort(key = lambda x : len(x)) # 길이별 정렬

for x in lst:
    print(x)