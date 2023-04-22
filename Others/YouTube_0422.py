import sys
input = sys.stdin.readline

n = int(input())        # 자연수 n입력
c = 0                   # 쌍의 개수
if 1 < n < 13:          # 두 주사위이므로 2~12사이의 숫자가 입력되어야 함
    for d1 in range(1,7):
        for d2 in range(1,7):
            if d1 + d2 >= n: # 두 주사위의 숫자 합이 n보다 크거나 같은 수일 경우
                print((d1,d2))
                c += 1
                if d1 == d2: # 두 주사위가 서로 같은 숫자인 경우
                    print('홍진호!')
    print(f'count = {c}')
else:                    # 답이 나올 수 없는 경우
    print('이럴거면 왜 시킨거야;;')