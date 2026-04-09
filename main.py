import sys

def get_menu_choice():
    while True:
        try:
            choice = input("선택: ").strip()
            if not choice:
                print("⚠️ 입력이 비어있습니다. 다시 입력해주세요.\n")
                continue
            choice_num = int(choice)
            if choice_num < 1 or choice_num > 5:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.\n")
                continue
            return choice_num
        except ValueError:
            print("⚠️ 잘못된 입력입니다. 숫자로 입력해주세요.\n")
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.")
            sys.exit(0)

def main():
    while True:
        print("========================================")
        print("        🎯 나만의 퀴즈 게임 🎯        ")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")
        
        choice = get_menu_choice()
        
        if choice == 1:
            print("\n📝 퀴즈 풀기 기능을 선택했습니다.\n")
        elif choice == 2:
            print("\n📌 퀴즈 추가 기능을 선택했습니다.\n")
        elif choice == 3:
            print("\n📋 퀴즈 목록 기능을 선택했습니다.\n")
        elif choice == 4:
            print("\n🏆 점수 확인 기능을 선택했습니다.\n")
        elif choice == 5:
            print("\n게임을 종료합니다. 안녕히 가세요!\n")
            break

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램을 안전하게 종료합니다.")
