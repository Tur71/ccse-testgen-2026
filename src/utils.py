
from dataclasses import dataclass
from typing import List, Dict
import random

@dataclass
class Question:
    id: str
    prompt: str
    options: List[str]
    correct: str
    theme: str | None = None


def select_questions(questions: List[Question], n: int, no_repeat: bool = True) -> List[Question]:
    if n <= 0:
        return []
    pool = questions.copy()
    if no_repeat:
        random.shuffle(pool)
        return pool[:min(n, len(pool))]
    else:
        return [random.choice(pool) for _ in range(n)]
