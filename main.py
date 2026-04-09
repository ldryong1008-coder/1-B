import sys
import random
from quiz import Quiz
from data import DEFAULT_QUIZZES

quizzes = DEFAULT_QUIZZES.copy()

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

def play_quiz():
    if not quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요.\n")
        return
        
    game_quizzes = quizzes.copy()
    random.shuffle(game_quizzes)
        
    print(f"\n📝 퀴즈를 시작합니다! (총 {len(game_quizzes)}문제)\n")
    print("-" * 40)
    
    score = 0
    for i, quiz in enumerate(game_quizzes, 1):
        quiz.display(i)
        
        while True:
            try:
                user_answer_str = input("정답 입력: ").strip()
                if not user_answer_str:
                    print("⚠️ 빈 입력입니다. 정답 번호를 입력해주세요.")
                    continue
                user_answer = int(user_answer_str)
                if user_answer < 1 or user_answer > len(quiz.choices):
                    print(f"⚠️ 1부터 {len(quiz.choices)} 사이의 번호를 입력해주세요.")
                    continue
                break
            except ValueError:
                print("⚠️ 잘못된 입력입니다. 숫자로 입력해주세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n게임 진행이 중단되었습니다.")
                return
                
        if quiz.check_answer(user_answer):
            print("✅ 정답입니다!\n")
            score += 1
        else:
            print(f"❌ 오답입니다! 정답은 {quiz.answer}번이었습니다.\n")
            
        print("-" * 40)
        
    total = len(quizzes)
    score_points = int((score / total) * 100) if total > 0 else 0
    print("========================================")
    print(f"🏆 결과: {total}문제 중 {score}문제 정답! ({score_points}점)")
    print("========================================")

def add_quiz():
    print("\n📌 새로운 퀴즈를 추가합니다.\n")
    try:
        question = input("문제를 입력하세요: ").strip()
        if not question:
            print("⚠️ 문제가 비어있습니다. 처음부터 다시 진행해주세요.\n")
            return

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            if not choice:
                print("⚠️ 선택지가 비어있습니다. 처음부터 다시 진행해주세요.\n")
                return
            choices.append(choice)

        answer_str = input("정답 번호 (1-4): ").strip()
        if not answer_str:
            print("⚠️ 정답 입력이 비어있습니다. 처음부터 다시 진행해주세요.\n")
            return
            
        answer = int(answer_str)
        if answer < 1 or answer > 4:
            print("⚠️ 1에서 4 사이의 숫자로 정답을 입력해주세요.\n")
            return
            
        new_quiz = Quiz(question=question, choices=choices, answer=answer)
        quizzes.append(new_quiz)
        print("\n✅ 퀴즈가 추가되었습니다!\n")
    except ValueError:
        print("⚠️ 잘못된 입력입니다. 정지에 숫자를 입력해주세요.\n")
    except (KeyboardInterrupt, EOFError):
        print("\n퀴즈 추가가 중단되었습니다.")

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
            play_quiz()
        elif choice == 2:
            add_quiz()
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
