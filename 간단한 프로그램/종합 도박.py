import random
import time as t
batting = 10000
user_batting = 0

class Game:
    def __init__(self):
        pass

    def rpc(self):

        computer =["주먹", "가위", "보"]
        gogo = "Y"

        global batting
        global user_batting

        print("나의 금액 : %d"%batting)
        while gogo == "Y" or gogo == "y" and batting != 0:
            user_batting = int(input("금액을 입력해 주세요 : "))
            if(user_batting > batting):
                print("금액이 큽니다")
                continue
            user = input("가위~바위~보! : ")

            computer_result = random.choice(computer)
            print(computer_result)

            if(user == "주먹" or user == "가위" or user == "보"):
                if(computer_result == "주먹" and user == "보") or (computer_result == "가위" and user == "주먹") or (computer_result == "보" or user == "가위"):
                    batting += user_batting
                    print("플레이어가 승리하셨습니다.\n현재 돈%d"%batting)
                    gogo = input("다시 하시겠습니까 ?(Y,N) : ")
                elif(computer_result == user):
                    print("무승부 입니다.")
                    gogo = input("다시 하시겠습니까 ?(Y,N) : ")
                else:
                    batting -= user_batting
                    print("플레이어가 패배하셨습니다.\n현재 돈%d"%batting)
                    gogo = input("다시 하시겠습니까 ?(Y,N) : ")
            else:
                print("다시 입력해 주세요")
                continue
        if(batting == 0):
            print("탕진입니다. 당신은 모든 돈을 다~~~ 날렸습니다")
        else:
            print("오늘 내가 번 돈은 %d입니다."%batting)
        

    def oe(self):
        global user_batting
        global batting

        gogo = "Y"

        while gogo == "y" or gogo == "Y" and batting != 0:
            ran_number = random.randint(1, 100)

            print("나의 금액 : %d"%batting)
            user_batting = int(input("금액을 입력해 주세요 : "))
            if(user_batting > batting):
                    print("금액이 큽니다")
                    continue
            choice = input("홀? 짝? : ")

            if ran_number % 2 == 0:
                print("짝수입니다")
            else:
                print("홀수입니다.")

            if (choice == "짝수" and ran_number % 2 == 0) or (choice == "홀수" and ran_number % 2 != 0):
                batting += user_batting
                print("성공입니다.\n현재 돈은 %d"%batting)
                gogo = input("다시 하시겠습니까 ?(Y,N) : ")
            else:
                batting -= user_batting
                print("실패입니다.\n현재 돈은 %d"%batting)
                gogo = input("다시 하시겠습니까 ?(Y,N) : ")

        if(batting == 0):
            print("탕진입니다. 당신은 모든 돈을 다~~~ 날렸습니다")
        else:
            print("오늘 내가 번 돈은 %d입니다."%batting)

    def re(self):
        global batting
        global user_batting

        hores = 0
        elephant = 0
        cow = 0
        sheep = 0

        print("나의 금액 : %d"%batting)
        while True:
            user_batting = int(input("금액을 입력해 주세요 : "))
            if(user_batting > batting):
                print("금액이 큽니다")
                continue
            ch = input("누가 우승할까? (말, 코끼리, 소, 양) : ")
            break


        while hores < 100 or elephant < 100 or cow < 100 or sheep < 100:
            if(hores < 100 and elephant < 100 and cow < 100 and sheep < 100):
                hores += random.randint(1, 10)
                elephant += random.randint(1, 10)
                cow += random.randint(1, 10)
                sheep += random.randint(1, 10)
                t.sleep(1)

                print(f"\r말 : {hores} 코끼리 : {elephant} 소 : {cow} 양 : {sheep}", end="")
            else:
                break



        result = max(hores, elephant, cow, sheep)

        if(result == hores):
            print("\n\n\n우승은 말 입니다.")
            if(ch == "말"):
                batting += user_batting
                print("맞추기를 성공하셨습니다.\n현재 돈%d"%batting)
            else:
                batting -= user_batting
                print("맞추기를 실패하셨습니다.\n현재 돈%d"%batting)
        elif(result == elephant):
            print("\n\n\n우승은 코끼리 입니다.")
            if(ch == "코끼리"):
                batting += user_batting
                print("맞추기를 성공하셨습니다.\n현재 돈%d"%batting)
            else:
                batting -= user_batting
                print("맞추기를 실패하셨습니다.\n현재 돈%d"%batting)
        elif(result == cow):
            print("\n\n\n우승은 소 입니다.")
            if(ch == "소"):
                batting += user_batting
                print("맞추기를 성공하셨습니다.\n현재 돈%d"%batting)
            else:
                batting -= user_batting
                print("맞추기를 실패하셨습니다.\n현재 돈%d"%batting)
        else:
            print("\n\n\n우승은 양 입니다.")
            if(ch == "양"):
                batting += user_batting
                print("맞추기를 성공하셨습니다.\n현재 돈%d"%batting)
            else:
                batting -= user_batting
                print("맞추기를 실패하셨습니다.\n현재 돈%d"%batting)
        if(batting == 0):
            print("탕진입니다. 당신은 모든 돈을 다~~~ 날렸습니다")



my = Game()
mm = "Y"
while mm == "Y" or mm == "y":
    print("1. 가위 바위 보(rpc)")
    print("2. 홀 짝 게임(oe)")
    print("3. 1등 맞추기(re)")
    my_choice = input("어떤한 게임을 하시겠습니까? : ")

    if(my_choice == "1"):
        my.rpc()
        mm = input("다른 게임을 하시겠습니까?(Y,N) : ")
    elif(my_choice == "2"):
        my.oe()
        mm = input("다른 게임을 하시겠습니까?(Y,N) : ")
    elif(my_choice == "3"):
        my.re()
        print("\n이 게임은 연속해서 할 수 없습니다.")
        mm = input("다른 게임을 하시겠습니까?(Y,N) : ")
    else:
        print("잘못된 입력입니다.")
        continue