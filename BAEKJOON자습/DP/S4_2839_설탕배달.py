x = int(input())

# DP테이블 초기화 
d = [5001] * (x+5) # n의 범위보다 하나 큰 값 # +5: index 오류 방지

# 3이나 5인 경우 1번
d[3] = d[5] = 1 

# DP - Bottom Up
for i in range(6,x+1):
    # 3kg와 5kg 중 최소 횟수를 선택한 후, 횟수 한 번을 더함
    d[i] = min(d[i-3], d[i-5]) + 1
    
# 계산이 가능한 경우 출력, 아닐 시 -1
print(d[x] if d[x]<5001 else -1)