import random
player_score=0
computer_score=0
#展示游戏界面
print('''
* * * * * * * 欢迎来到4399游戏平台 * * * * * * *
              石头   剪刀    布
* * * * * * * * * * * * * * * * * * * * * * * 
''')
#进行玩家和电脑的角色选择
player_name=input('输入玩家姓名：')
print('1.佐助 2.鸣人 3.小樱 4.自定义电脑角色')
choice = 0
while not 1 <= choice <= 4:
    try:#防止输入错误
        choice = int(input("请输入1到4的数字选择角色："))
        if choice == 1:
            computer_name = '佐助'
        elif choice == 2:
            computer_name = '鸣人'
        elif choice == 3:
            computer_name = '小樱'
        elif choice == 4:
            computer_name = input('自定义电脑角色: ')
        else:
             print('请按以下标准重新输入')
    except ValueError:
        print('请按以下标准重新输入')
print(player_name,'VS',computer_name)
#实现循环对战并计分
while True:
    player_fist=0
    while not 1 <= player_fist <=3:
        try:
            player_fist = int(input('--------------请选择 1.石头 2.剪刀 3.布------------------\n'))
            if player_fist==1:
                player_fist_name='石头'
            elif player_fist==2:
                player_fist_name='剪刀'
            elif player_fist==3:
                player_fist_name='布'
            else:
                print('请按以下要求选择')
        except ValueError:
             print('请按以下要求选择')
    computer_fist=random.randint(1,3)
    if computer_fist==1:
        computer_fist_name='石头'
    elif computer_fist==2:
        computer_fist_name='剪刀'
    else :
        computer_fist_name='布'
    print(player_name,'出拳:',player_fist_name)
    print(computer_name,'出拳:',computer_fist_name)
    if player_fist==computer_fist:
        print('平局')
    elif (player_fist==1 and computer_fist==2) or (player_fist==2 and computer_fist==3) or (player_fist==3 and computer_fist==1):
        print('玩家',player_name,'胜')
        player_score+=1
    else:
        print('电脑',computer_name,'胜')
        computer_score+=1
    answer=input('是否继续y/n\n')
    #显示最终输赢结果
    if answer=='n':
        if computer_score>player_score:
            print('---------------------最终结果--------------------------')
            print(computer_name, computer_score)
            print(player_name, player_score)
            print(computer_name, '赢')
        elif player_score>computer_score:
            print('---------------------最终结果-----------------------------')
            print(computer_name, computer_score)
            print(player_name, player_score)
            print(player_name, '赢')
        else:
            print('---------------------最终结果-----------------------------')
            print(computer_name, computer_score)
            print(player_name, player_score)
            print(computer_name,'平局',player_name)
        break






