# <Game1. 화가 나서 야생의 팽도리로 변해 버린 호니를 달래주어라!>
# 룰은 다음과 같다. 야생의 팽도리로 변신한 호니는 사용자와 3단계에 걸친 대결을 시작한다.
# 사용자는 3개의 life를 가지며, 3개를 모두 소진할 시 호니를 달래주는 것을 실패하여...(생략)
# 각 단계의 게임은 1번씩만 클리어하면 된다. 2단계에서 실패할 시 다시 2단계부터 시작한다.
# 1단계의 게임은 단순한 가위바위보이지만 남자친구는 져주어야 하기 때문에 져야만 통과할 수 있다. 비기면 다시 시작하며, 이길 시 1개의 life가 소멸된다.
# 2단계의 게임은 호니에 대한 4가지 퀴즈를 맞추는 것으로, 문제와 함께 객관식 4지선다가 나온다. 한 번이라도 틀릴 시, 1개의 life가 소멸된다.
# 3단계의 게임은 절대로 몰라서는 안되는 기념일의 날짜에 대한 문제가 나온다. 그렇기에 틀릴 시 2개의 life가 소멸된다.

# variance
import random
life = 3                # 사용자의 초기 생명
clearState = [False]*4  # 클리어의 유무 확인
stage2Q = ['<다음 중 호니가 좋아하는 아이스크림이 아닌 것은?>', '<다음 중 호니가 좋아하는 사탕의 맛은?>', '<다음 중 호니가 사준 비건 빵의 브랜드명과 제품명은?>', '<다음 중 가장 예쁜 사람은?>'] 
stage2A = ['1.생귤탱귤감귤 2.옥동자 3.뉴치케 4.체리마루', '1.포도 2.레몬 3.오렌지 4.파인애플', '1.망넛이네 쌉사루니 2.망넛이네 찹싸루니 3.망원동 찹쌀떡 4.망리단길 찹쌀떡', '1.호은이 2.곽호은 3.호니 4.내 여자친구']
stage2answer = [4,3,2,(1,2,3,4)]
stage3Q = ['<300일은 얼마 안남았으니까 당연히 알겠지?>', '<그럼 1주년은?>', '<500일까지 맞추면 진짜 봐줄게 ㅎ.ㅎ>']
stage3answer = [[5,4,'목'],[7,8,'토'],[11,20,'월']]

# introduction
print('[호니]:오빠는 6시간 동안 내 말은 듣지도 않고 코딩만 해...됐어. 나도 변할거야.')
print('<Game1 Start! - 야생의 팽도리가 나타났다!>')
username = input('사용자의 이름을 입력하시오: ')
print('*'*50)

# stage1 function
def stage1(life):
    print('[야생의 팽도리]: 설마 나를 이겨먹지는 않겠지? 시작은 가위바위보!')
    rn = random.randint(1,3)    # 가위(1), 바위(2), 보(3)
    temp = False                # 승패를 저장
    # 팽도리 가위바위보 설정
    if rn == 1:
        paeng = '가위'
    elif rn == 2:
        paeng = '바위'
    else:
        paeng = '보'
    # 유저 입력    
    print(f'[야생의 팽도리]: 참고로 난 {paeng}를 낼거야! 믿어.')
    answer = input(f'{username}님, 가위바위보 중 하나를 선택하세요: ')
    # 승패 확인
    if rn == 1:
        if answer == '가위':
            temp = 2            # 무승부
        elif answer == '보':
            temp = True
    elif rn == 2:
        if answer == '바위':
            temp = 2
        elif answer == '가위':
            temp = True
    else:
        if answer == '보':
            temp = 2
        elif answer == '바위':
            temp = True        
    # 결과 출력        
    if temp == True:
        print('[야생의 팽도리]: 이번에는 눈치가 빨랐네. 앞으로도 이렇게 좀 져줘 ㅡㅡ 1단계는 통과야.')
        print('*'*50)
        clearState[1] = True # 1단계 통과
    elif temp == 2:
        print(f'[야생의 팽도리]: 내가 {paeng}낸다고 했잖아!! 다시 해.')
        print('*'*50)
    else:
        print('[야생의 팽도리]: 아니 나를 못 믿은거야? 한 대 맞아.')
        print(f'<{username}의 life가 1개 소멸되었습니다.>')
        print('*'*50)
        life -= 1
        
# stage2 function
def stage2(life):
    print('[야생의 팽도리]: 우리 만난지 거의 300일인데,, 이것도 모르면 안되겠지?^^')
    for i in range(len(stage2Q)):
        print(stage2Q[i])
        print(stage2A[i])
        answer = int(input(f'{username}님, 보기 중 답을 선택해주세요: '))
        if answer  == stage2answer[i]:
            print("[야생의 팽도리]: 그래. 이정도는 맞춰야지.")
            print('*'*50)
        elif i == 3:
            if answer:
                print("[야생의 팽도리]: 잘 알고 있네. 알면 잘해! 2단계 통과 축하해.")
                print('*'*50)
                clearState[2] = True # 2단계 통과
        else:
            print("[야생의 팽도리]: 안되겠다. 더 공부해서 와! 그리고 한 대 맞자.")
            print(f'<{username}의 life가 1개 소멸되었습니다.>')
            print('*'*50)
            life -= 1
            break
 
# stage3 function
def stage3(life):
    print('[야생의 팽도리]: 대망의 마지막 단계야. 틀리면 큰일날..걸..?')         
    for i in range(len(stage3Q)):
        print(stage3Q[i])
        print(f'{username}님, 월 & 일 & 요일을 공백으로 구분지어 답해주세요: ', end = '')
        answer = input().split()
        if int(answer[0]) == stage3answer[i][0] and int(answer[1]) == stage3answer[i][1] and answer[2] == stage3answer[i][2]:
            print('[야생의 팽도리]: 오호..정답이야..알고 있네..?')
            print('*'*50)
            clearState[3] = True
        else:
            print('[야생의 팽도리]: 내가 틀리면 큰일난다고 했지?^^') 
            print(f'<{username}의 life가 2개 소멸되었습니다.>')
            print('*'*50)
            life -= 2
            break
    if clearState[3]:
        print('[야생의 팽도리]: 다 맞출줄은 몰랐는데 의외네..축하해! 3단계까지 모두 통과했어.')
        print('*'*50)
        print('<Game1 End! - 야생의 팽도리를 성공적으로 달래주었습니다!>')
        print('*'*50)
        print('<게임을 종료합니다...>')
        exit(0) # 게임 종료
        
# main
while life:
    # stage1 실행
    if clearState[1]:
        print('[야생의 팽도리]: 1단계정도는 통과해야지. 2단계부터 시작하면 돼.')
        print('*'*50)
        # stage2 실행
        if clearState[2]:
            print('[야생의 팽도리]: 거의 다 왔네. 분발해봐.')
            print('*'*50)
            # stage3 실행
            stage3(life) 
        else:
            stage2(life)
    else:
        stage1(life)