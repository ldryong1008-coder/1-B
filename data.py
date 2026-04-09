from quiz import Quiz

DEFAULT_QUIZZES = [
    Quiz(
        question="마블 시네마틱 유니버스에서 타노스가 모은 인피니티 스톤의 개수는?",
        choices=["4개", "5개", "6개", "7개"],
        answer=3,
        hint="캡틴 아메리카의 방패처럼 둥근 형태가 아닌, 타임 스톤까지 포함한 보석의 총 개수입니다."
    ),
    Quiz(
        question="영화 '기생충'의 감독은?",
        choices=["박찬욱", "봉준호", "김기덕", "이창동"],
        answer=2,
        hint="설국열차, 괴물 등의 작품도 만들었습니다."
    ),
    Quiz(
        question="영화 '인터스텔라'에서 주인공이 방문하지 않은 행성은?",
        choices=["밀러 행성", "만 행성", "에드먼즈 행성", "가르강튀아 내부 행성"],
        answer=4,
        hint="밀러 행성은 물의 별, 만 행성은 얼음의 별, 에드먼즈 행성은 아멜리아가 마지막에 남은 곳입니다."
    ),
    Quiz(
        question="다음 중 해리포터 시리즈에서 가장 먼저 개봉한 영화는?",
        choices=["비밀의 방", "불의 잔", "마법사의 돌", "아즈카반의 죄수"],
        answer=3,
        hint="해리가 호그와트에 입학하는 첫 편의 제목입니다."
    ),
    Quiz(
        question="영화 '매트릭스'에서 네오가 선택해 먹은 진실의 알약 색깔은?",
        choices=["빨간 약", "파란 약", "노란 약", "초록 약"],
        answer=1,
        hint="모피어스가 거짓에서 깨어나 진실을 보게 해준다고 내민 약입니다."
    )
]

def get_default_quizzes_dict() -> list:
    """JSON으로 저장하기 쉽도록 딕셔너리 리스트로 반환"""
    return [quiz.to_dict() for quiz in DEFAULT_QUIZZES]
