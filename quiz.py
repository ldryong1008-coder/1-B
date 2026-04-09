class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int):
        """
        :param question: 퀴즈 문제
        :param choices: 4개의 선택지 리스트
        :param answer: 정답 번호 (1-4)
        """
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, index: int = None):
        """퀴즈를 화면에 출력합니다."""
        if index is not None:
            print(f"\n[{index}번 문제]")
        print(f"{self.question}\n")
        
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")
            
    def check_answer(self, user_answer: int) -> bool:
        """사용자의 정답이 맞는지 확인합니다."""
        return self.answer == user_answer

    def to_dict(self) -> dict:
        """JSON 저장을 위해 딕셔너리로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data: dict):
        """딕셔너리에서 Quiz 인스턴스를 생성합니다."""
        return cls(
            question=data.get("question", ""),
            choices=data.get("choices", []),
            answer=data.get("answer", 1)
        )
