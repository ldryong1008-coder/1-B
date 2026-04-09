import json
import random
import os
from quiz import Quiz
from data import get_default_quizzes_dict

STATE_FILE = "state.json"

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_state()

    def load_state(self):
        """state.json에서 데이터를 불러옵니다. 없으면 기본 데이터를 사용합니다."""
        if not os.path.exists(STATE_FILE):
            print("📂 데이터 파일이 없습니다. 기본 퀴즈를 불러옵니다.")
            self._load_default()
            return
            
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            quizzes_data = data.get("quizzes", [])
            self.best_score = data.get("best_score", 0)
            
            for q_data in quizzes_data:
                self.quizzes.append(Quiz.from_dict(q_data))
                
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
        except (json.JSONDecodeError, Exception) as e:
            print(f"⚠️ 데이터 파일이 손상되었습니다. 기본 상태로 시작합니다. ({str(e)})")
            self._load_default()

    def _load_default(self):
        """기본 데이터를 로드합니다."""
        self.quizzes = []
        for q in get_default_quizzes_dict():
            self.quizzes.append(Quiz.from_dict(q))
        self.best_score = 0
        self.save_state()

    def save_state(self):
        """현재 데이터를 state.json에 저장합니다."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }
        try:
            with open(STATE_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"⚠️ 데이터 저장 중 오류가 발생했습니다: {str(e)}")

    def play(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요.\n")
            return
            
        game_quizzes = self.quizzes.copy()
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
                    self.save_state()
                    return
                    
            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!\n")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번이었습니다.\n")
                
            print("-" * 40)
            
        total = len(game_quizzes)
        score_points = int((score / total) * 100) if total > 0 else 0
        print("========================================")
        print(f"🏆 결과: {total}문제 중 {score}문제 정답! ({score_points}점)")
        if score_points > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score_points
            self.save_state()
        print("========================================")

    def add_quiz(self):
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
            self.quizzes.append(new_quiz)
            self.save_state()
            print("\n✅ 퀴즈가 추가되었습니다!\n")
        except ValueError:
            print("⚠️ 잘못된 입력입니다. 1-4 숫자를 입력해주세요.\n")
        except (KeyboardInterrupt, EOFError):
            print("\n퀴즈 추가가 중단되었습니다.")
            self.save_state()

    def list_quizzes(self):
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.\n")
            return
            
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40 + "\n")

    def show_score(self):
        print("\n🏆 점수 확인")
        print(f"현재 최고 점수: {self.best_score}점\n")
