# 🎯 나만의 퀴즈 게임 (My Quiz Game)

초보자도 쉽게 즐기고 배울 수 있는 **터미널 기반 파이썬 퀴즈 게임**입니다. 
프로그래밍 언어를 배우는 가장 확실한 방법은 직접 프로그램을 만들어보는 것입니다! 이 프로젝트는 파이썬(Python)의 기본 문법과 객체 지향(클래스), 그리고 파일 입출력을 활용하여 만들어졌으며, Git을 통한 버전 관리의 흔적을 고스란히 담고 있습니다.

---

## 📖 1. 프로젝트 개요
터미널 환경에서 실행되는 퀴즈 게임 프로그램입니다. 
파이썬 언어의 핵심 개념(조건문, 반복문, 클래스와 객체, JSON 파일 처리)을 바탕으로 설계되었으며, 올바르지 않은 사용자 입력(예: 문자 입력, 빈칸 등)에도 프로그램이 튕기거나 비정상 종료되지 않도록 견고하게 예외 처리(`try/except`)가 되어있습니다. 프로그램 종료 중에도 안전한 상태 저장을 보장합니다.

---

## 🎬 2. 퀴즈 주제 선정 이유
본 퀴즈 게임의 기본 주제는 **'영화 (Movie)'** 입니다.
마블 시네마틱 유니버스(타노스), 기생충, 인터스텔라 등 대중적으로 유명한 영화 지식들을 문제로 구성하였습니다. 누구나 가볍고 즐겁게 프로그래밍의 결과를 테스트해 볼 수 있도록 가장 친숙한 주제를 선정했습니다.

---

## 💻 3. 실행 방법
이 프로그램은 외부 라이브러리 설치 없이 순수 파이썬의 기본 기능만을 사용합니다.

1. 컴퓨터에 파이썬(Python 3.10 이상 권장)이 올바르게 설치되어 있는지 확인합니다.
2. 터미널(명령 프롬프트)을 열고, 본 프로젝트 폴더 안으로 이동합니다.
3. 아래의 명령어를 입력하여 게임을 실행합니다.
   ```bash
   python main.py
   ```

---

## 📋 4. 주요 기능 목록
프로그램을 실행하면 화면에 메뉴가 나타납니다. 사용자는 1~6번의 기능을 아래와 같이 수행할 수 있습니다.

```yaml
[1. 퀴즈 풀기]
  - 특징: 무작위(Random) 섞임 출제 및 원하는 문항 개수 직접 선택 가능
  - 채점: 문항당 기본 획득 점수 10점
  - 힌트 시스템: 풀이 중 '0'번 입력 시 힌트가 등장하며, 정답을 맞출 시 5점으로 감점 반영

[2. 퀴즈 추가]
  - 특징: 문제 화면 내에서 질문, 보기 4개, 정답, 힌트 문구를 입력하여 영원히 보관해 둘 나만의 커스텀 퀴즈 생성

[3. 퀴즈 목록] & [4. 퀴즈 삭제]
  - 특징: 현재 DB에 등록된 전체 퀴즈 구조를 조회하고, 불필요해진 고유 퀴즈 번호를 타진해 파일을 날려버리는 기능

[5. 점수 및 히스토리]
  - 특징: 본인의 전체 누적 최고 점수(Best Score) 갱신과, 최근 5회차의 플레이 이력(날짜/시간, 문제 수, 획득 기록) 출력

[6. 종료]
  - 동작: 현재까지의 상태 변동 내역을 state.json 파일에 실시간으로 기록(Save) 후 안전하게 터미널 종료
```

> ⚠️ 잘못된 숫자(예: 9번 입력), 문자의 오입력, 빈칸(`Enter`), `Ctrl+C` 등 어떠한 비정상 입력 상황이 발생해도 프로그램은 사용자 안내 메시지를 구동하며 안전하게 방어해냅니다.

---

## 📂 5. 파일 구조 설명
프로그램을 구성하는 핵심 파일들은 객체 지향 및 아키텍처 관점에 입각하여 철저히 역할별로 분리되어 있습니다.

```text
📦 1-B Project Directory
 ┣ 📜 main.py       # [Entry Point] 메인 구동 파일 / 콘솔 UI 루프 처리 및 예외 통제
 ┣ 📜 game.py       # [Controller] 퀴즈 채점, 파일 입출력, 게임 흐름(QuizGame 클래스) 중앙 총괄
 ┣ 📜 quiz.py       # [Model] 개별 문제 정보 및 힌트를 보관하는 데이터(Quiz 클래스) 모델
 ┣ 📜 data.py       # [Fallback] 초기 시작 또는 파일 폭파 시 복구에 쓰일 5종의 시드(Seed) 데이터
 ┣ 📜 state.json    # [Storage] 점수와 퀴즈 이력이 실시간으로 파싱되는 서버 로컬 데이터베이스
 ┗ 📜 .gitignore    # [Config] Git 저장소 백업 추적에서 파이썬 캐시 파일 등 불필요 항목을 깔끔히 제외
```

---

## 💾 6. 데이터 파일 (`state.json`) 설명
- **경로**: 프로젝트 최상위 폴더에 위치 (개발자가 처음 실행할 때 자동으로 모습을 드러냅니다)
- **역할**: 프로그램을 껐다가 나중에 다시 켜더라도 여러분이 **새로 추가했던 퀴즈**들과 영광스러운 **최고 점수 및 모든 히스토리**가 그대로 유지되도록 만들어주는 소중한 "데이터 저장고"입니다.
- **스키마 (구조) 예시 살펴보기**: (UTF-8 인코딩)
```json
{
    "quizzes": [
        {
            "question": "Python의 창시자는?",
            "choices": ["Guido", "Linus", "Bjarne", "James"],
            "answer": 1,
            "hint": "네덜란드 출신의 천재가 취미로 만든 언어입니다."
        }
    ],
    "best_score": 50,
    "history": [
        {
            "date": "2026-04-09 18:05:01",
            "questions": 5,
            "score": 50
        }
    ]
}
```

---

## 📸 7. 프로그램 실행 결과 (스크린샷)

위에서 안내한 기능들이 실제로 어떻게 이뤄지는지 시각적으로 증명하는 자료입니다. (과제 제출 필수 스크린샷 캡쳐분)

- **개발 환경 설정 증빙 (VSCode 및 파이썬 버전 등)**

  <img width="752" height="250" alt="Screenshot 2026-04-09 at 7 39 25 PM" src="https://github.com/user-attachments/assets/0ef22e73-4cf2-4c59-a639-449aaed0706c" />


- **메인 메뉴 화면**

  <img width="301" height="160" alt="Screenshot 2026-04-09 at 7 28 43 PM" src="https://github.com/user-attachments/assets/0afd1e81-d3ec-4265-9bf3-69be3fd2307e" />

- **퀴즈 풀기 진행 화면**

  <img width="429" height="221" alt="Screenshot 2026-04-09 at 7 29 50 PM" src="https://github.com/user-attachments/assets/5c6f062c-1cec-4710-97fe-6b91c4bea762" />

- **새로운 퀴즈 추가 화면**

  <img width="321" height="181" alt="Screenshot 2026-04-09 at 7 31 28 PM" src="https://github.com/user-attachments/assets/5e16be4c-2f7e-4c84-b114-d615084f60ca" />

- **내 기록/점수 확인 (스코어보드)**

  <img width="624" height="301" alt="Screenshot 2026-04-09 at 7 27 59 PM" src="https://github.com/user-attachments/assets/03c6264e-77c6-4e36-a3da-961af46e3f16" />

- **의미있는 Git Log 이력 증빙** (`git log --oneline --graph` 수행 결과)

  <img width="624" height="284" alt="Screenshot 2026-04-09 at 7 26 19 PM" src="https://github.com/user-attachments/assets/e920e8dc-88ce-4939-87c6-6223fe58446a" />

---

## 🚀 8. 단계별 기능 구현 타임라인 (Development Steps)

본 프로그램이 어떠한 고민과 설계 흐름으로 밑바닥부터 견고하게 조립되었는지 보여주는 7단계의 개발 타임라인입니다.

### [Step 1] Initial Setup (환경 설정 및 뼈대 구축)
역할 분산을 위해 핵심 파일 3개를 분할 생성하고, 애플리케이션 진입점(`main.py`)에 무한 루프와 예외 처리를 결합하여 사용자의 비정상 입력을 원천 차단하는 텍스트 UI 메뉴망을 구축했습니다.
```python
while True:
    print("\n--- 🎬 영화 퀴즈 게임 ---")
    print("1. 퀴즈 풀기   2. 퀴즈 추가 ... 6. 종료")
    try:
        choice = input("원하는 번호를 입력: ").strip()
        if choice == '6': break
    except Exception as e:
        print(f"오류: {e}")
```

### [Step 2] Class & Model (데이터 모델의 정의)
`quiz.py`에 개별 문제 정보를 규격화하는 `Quiz` 데이터 객체(Model)를 선언하고, 추후 JSON 통신을 위한 직렬화(Serialization) 메서드를 구현했습니다.
```python
class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def to_dict(self):
        # JSON 직렬화를 위한 딕셔너리 리턴
        return {"question": self.question, "choices": self.choices, "answer": self.answer, "hint": self.hint}
```

### [Step 3] Data Persistence (JSON I/O 기초 연동)
`game.py`의 `QuizGame` 컨트롤러 클래스에 `state.json` 물리 파일을 읽고 쓰는 입출력(I/O) 함수를 탑재하여, 프로그램이 꺼지더라도 데이터가 휘발되지 않도록 영속성을 부여했습니다.
```python
def save_state(self):
    state = {
        "quizzes": [q.to_dict() for q in self.quizzes],
        "best_score": self.best_score,
        "history": self.history
    }
    with open('state.json', 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=4)
```

### [Step 4] Quiz CRUD (퀴즈 추가 및 삭제)
객체를 동적으로 생성하여 내부 리스트(`quizzes`)에 등록하거나, 리스트의 `pop()` 메서드를 응용해 지정 번호의 항목을 조준 삭제(C/D)하는 로직을 결합했습니다.
```python
def add_quiz(self):
    new_quiz = Quiz(question, choices, answer, hint)
    self.quizzes.append(new_quiz)
    self.save_state()  # 즉시 파일 보존

def delete_quiz(self):
    deleted = self.quizzes.pop(idx)
    self.save_state()  # 즉시 파일 삭제 반영
```

### [Step 5] Core Gameplay Logic (방어형 풀기 로직)
보유 퀴즈들을 반복문(`for`)으로 꺼내어 콘솔에 렌더링하고, 유저의 기입 답안과 실제 `quiz.answer`를 실시간 대조하여 점수를 누적시키는 메인 비즈니스 로직을 가동했습니다.
```python
for i, quiz in enumerate(selected_quizzes, 1):
    print(f"\nQ{i}. {quiz.question}")
    
    user_ans = int(input("정답 번호: "))
    if user_ans == quiz.answer:
        print("정답입니다!")
        score += 10
```

### [Step 6] Advanced Features (보너스 기능 강화)
랜덤 모듈, 힌트 배점 패널티 분기점, `datetime` 기반 다이나믹 플레이 기록 등 고도화 기술을 프로그램 곳곳에 접목시켰습니다.
```python
# 1. 무작위 섞기 및 리스트 슬라이싱(원하는 갯수)
random.shuffle(self.quizzes)
selected = self.quizzes[:num]

# 2. 힌트 시스템 및 감점 분기
if user_ans == 0:
    print(f"💡 힌트: {quiz.hint}")
    # 힌트를 본 후 정답을 맞출 경우 score += 5 획득으로 규칙 변경

# 3. 동적 히스토리 5개 한정 덱(Deque) 스타일 저장
self.history.insert(0, {
    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "score": score
})
self.history = self.history[:5]
```

### [Step 7] Robustness & Fallback (백업 및 자가 치유망 결합)
극한의 상황(`Ctrl+C` 비정상 셧다운, `JSONDecodeError` 파일 오염) 시 게임이 패닉에 빠지는 것을 막기 위해, 원본(`data.py`) 데이터를 긁어와 프로그램 스스로 회복을 꾀하는 최고봉 방어벽을 세웠습니다.
```python
except json.JSONDecodeError:
    print("\n경고: state.json 파일이 깨졌습니다. 복구를 시도합니다.")
    from data import get_default_quizzes_dict
    self.quizzes = [Quiz.from_dict(q) for q in get_default_quizzes_dict()]
    self.best_score = 0

except KeyboardInterrupt:
    print("\n플러그가 뽑혔습니다. 진행 상황을 비상 백업합니다.")
    self.save_state()
```

---

## 🌿 9. Git 워크플로우 통제 및 복제 실습 내용

본 프로젝트는 그저 코드를 짜는 것을 넘어 실무 팀 단위 코드 작성처럼 **Git** 이라는 형상 관리 도구를 철저하게 곁에 두고 관리되었습니다.

### ✅ 필수 7종 커맨드 + 복제/병합 실습 타임라인
과제를 수행하며 터미널(CLI) 환경에서 실제로 타이핑하며 익혔던 주요 Git 명령어들의 흐름 기록입니다. 총 7가지(`init`, `add`, `commit`, `push`, `pull`, `checkout`, `clone`)의 필수 명령어를 완벽히 체험했습니다.

**[Phase 1] 로컬 빌드 및 버전 기록**
```bash
# 1. 처음 폴더를 Git 저장소로 지정하기
git init

# 2. 파일 변경사항들 장바구니(Staging Area)에 담기
git add .
git add README.md

# 3. 작업 단위별로 의미 있는 메시지와 함께 확정(Commit) 짓기
git commit -m "Feat: 퀴즈 추가 및 삭제 기능 구현"
```

**[Phase 2] 안전한 가지치기 (Branching)**
```bash
# 4. 기능 실험을 위해 새로운 임시 브랜치를 만들고 즉시 이동하기
git checkout -b feature/play-quiz

# (기능 개발 완료 후) 다시 메인 줄기로 돌아와 안전하게 합치고 삭제하기
git checkout main
git merge feature/play-quiz
git branch -d feature/play-quiz
```

**[Phase 3] 원격 저장소 연동 및 통신**
```bash
# 5. 완성된 코드를 내 GitHub(원격 저장소)로 쏘아 올리기
git push origin main

# 6. 협업을 가상하여, 타 디렉토리에 원격 저장소 통째로 복제하기 (Clone 실습)
git clone https://github.com/ldryong1008-coder/1-B.git 1-B-practice

# 7. 원격 저장소에서 외부(가상 동료)가 수정한 최신 내역을, 내 컴퓨터로 다시 당겨오기 (Pull 실습)
git pull origin main
```
> **💡 복제 및 병합 실습 성과**: 수동으로 코드를 긁어 복사하는 것이 아니라 `git clone`과 `git pull` 명령어를 통해 원격 클라우드 서버와 로컬 컴퓨터 간의 코드가 완벽히 동기화(Sync)되는 형상 관리의 쾌감을 직접 확인하고 터득했습니다! 

---

## 💡 10. 아키텍처 및 핵심 개념 Q&A (평가 기준 검증)

본 프로젝트를 구현하며 다듬어진 필수 파이썬/Git 개념들과 설계 결정들에 대한 핵심 요약 풀이입니다.

### 📂 1. 클래스 설계 및 로직 분리 (평가기준 8, 9, 13, 20)
| 평가 기준 / 핵심 문답 | 구현 근거 및 핵심 설명 |
| :--- | :--- |
| **`Quiz` & `QuizGame`의 책임 분리** | `Quiz`는 문항 유지와 정답 채점을 다루는 **데이터 모델**이고, `QuizGame`은 사용자 입력을 제어하고 점수를 통제하는 **게임 컨트롤러**입니다. |
| **로직 분리 기준** | **입력 검증**은 앞단(`while True` + `try/except`)에서 악성 데이터를 방어하고, **게임 진행** 로직은 중앙 집중화시켰으며, 파일 저장 등 **데이터 처리**는 별도로 격리(`save/load`)시켜 상호 의존성을 낮췄습니다. |
| **클래스(객체) 사용 이유** | 퀴즈 배열 형식이 아무리 방대해져도 관련된 데이터와 메서드를 하나의 캡슐(인스턴스)에 안전하게 묶어둘 수 있어 변수 오염을 막고 유지보수가 쉬워집니다. |
| **수정 포인트의 명확화** | 게임 구조 변화(예: 주관식 변경)는 `quiz.py`를, 채점 규칙의 변화는 `game.py`를 수정하면 되도록 역할을 명확히 쪼개었습니다. |

### 💾 2. JSON 데이터 통제 (평가기준 10, 14, 17, 18)
| 평가 기준 / 핵심 문답 | 구현 근거 및 핵심 설명 |
| :--- | :--- |
| **JSON 파일 포맷 활용 이유** | 텍스트 형태인지라 파이썬의 핵심인 리스트/딕셔너리 구조와 직렬화/역직렬화가 1:1로 정확하게 호환되어 가장 직관적이고 편리합니다. |
| **`state.json` 스토리지 사이클** | 프로그램 실행 시 최초 1회 **불러오기(load)**를 진행하고, 점수나 문제가 바뀌거나 정상 종료할 때마다 즉시 **저장(save)**을 호출하여 단 1건의 플레이 데이터도 잃지 않습니다. |
| **확장성 높은 스키마 설계** | 전체를 최상위 오브젝트 `{}` 구조로 감싸고 내부에 `quizzes`와 `history` 묶음을 배치했습니다. 훗날 설정 데이터가 추가되더라도 기존 구조가 전혀 깨지지 않는 견고한 방식입니다. |
| **방대한 누적 시의 한계점** | 파일 전체를 매번 덮어쓰는 로직은 데이터가 너무 큰 경우 메모리 과점유 및 Disk I/O 병목에 취약합니다. 실 서비스처럼 방대해진다면 반드시 데이터베이스(RDBMS 등) 도입이 권장됩니다. |

### 🛡️ 3. 예외 처리와 안전 종료 (평가기준 11, 15, 19)
| 평가 기준 / 핵심 문답 | 구현 근거 및 핵심 설명 |
| :--- | :--- |
| **`try/except`의 강력한 필요성** | 존재하지 않는 파일 읽기 등 코드 외적인 OS 차원의 예기치 못한 런타임 오류로 인해 유저의 게임이 갑자기 종료(Death)되는 치명적 현상을 완벽히 방어해 줍니다. |
| **비정상 종료 방어 (`Ctrl+C` 등)** | 사용자의 터미널 강제 종료 상황에서도, 에러 뿜어냄 대신 당장의 진행 상황을 일단 백업(`save_state`)시킨 뒤 안내문과 함께 깔끔하게 빠져나가는 우아한 종료(Graceful Shutdown)를 유도했습니다. |
| **JSON 파싱 손상 복구** | 사용자가 json 파일을 건들다 문법을 망가뜨렸을 경우(`JSONDecodeError`), 즉시 에러를 붙잡고 내장된 `data.py`(기본 5종) 복구본을 메모리에 띄워내는 훌륭한 백업망 기반이 존재합니다. |

### 🌿 4. Git 협업 워크플로우 (평가기준 12, 16)
| 평가 기준 / 핵심 문답 | 구현 근거 및 핵심 설명 |
| :--- | :--- |
| **의미있는 커밋 단위 분할** | `Feat`(기능), `Fix`(수정), `Docs`(문서), `Refactor`(구조개선) 등 규칙적인 접두사를 통해, 동료 개발자 누구나 타임라인을 한눈에 파악 가능하도록 작업 단위를 잘게 끊어 냈습니다. |
| **독립 브랜치 및 병합(Merge)** | 핵심인 메인 뼈대를 보호하고, 별도 가지(`feature`)에서 안전하게 새 작업을 검증 마친 뒤 원래 원본 코드로 합치게 하여 메인 시스템 붕괴 위험성을 완벽하게 배제하는 실무 플로우를 적용했습니다. |
