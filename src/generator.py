
import csv
from typing import List
from pathlib import Path
from .utils import Question

REQUIRED_COLUMNS = {"id", "pregunta", "opciones", "correcta"}


def load_csv_questions(csv_dir: str) -> List[Question]:
    base = Path(csv_dir)
    questions: List[Question] = []
    for csv_path in sorted(base.glob("*.csv")):
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
            if missing:
                raise ValueError(f"CSV {csv_path.name} missing columns: {missing}")
            for row in reader:
                opts = [o.strip() for o in (row.get("opciones", "").split("||")) if o.strip()]
                questions.append(
                    Question(
                        id=str(row.get("id", "")).strip(),
                        prompt=str(row.get("pregunta", "")).strip(),
                        options=opts,
                        correct=str(row.get("correcta", "")).strip(),
                        theme=(row.get("tema") or None)
                    )
                )
    return questions


def export_txt(questions: List[Question], dest_path: str):
    with open(dest_path, 'w', encoding='utf-8') as f:
        for i, q in enumerate(questions, 1):
            f.write(f"{i}. {q.prompt}
")
            for idx, opt in enumerate(q.options, 1):
                f.write(f"   {idx}) {opt}
")
            f.write("
")
